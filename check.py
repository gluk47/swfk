#! /usr/bin/python

import os
import re
import sys
import StringIO

pat = re.compile(r'\\begin{listing}\s*\\begin{verbatim}\s*(.*?)\\end{verbatim}', re.DOTALL | re.MULTILINE)

stdout = sys.stdout

def build_example(srclines, wantlines):
    for x in range(0, len(wantlines)):
        if wantlines[x].rstrip() == '(continues on...)':
            wantlines = wantlines[0:x]
            break
        
    return Example('\n'.join(srclines).lstrip().rstrip().replace('\r\n', '\n'), 
                   '\n'.join(wantlines).lstrip().rstrip().replace('\r\n', '\n')) 

def parse(source):
    examples = []
    src = []
    want = []
    parsing_src = False
    parsing_want = False
    for line in source.split('\n'):
        if line.startswith('>>> ') or line.startswith('...'):
            if parsing_want:
                examples.append(build_example(src, want))
                src = []
                want = []
            parsing_src = True
            src.append(line[4:])
        elif not parsing_src and not parsing_want:
            continue
        else:
            want.append(line)
            parsing_want = True
    if len(src) > 0:
        examples.append(build_example(src, want))
    return examples
    

class Example(object):
    def __init__(self, source, want):
        self.source = source
        self.want = want

    def __str__(self):
        return 'src=\n%s\nwant=\n%s' % (self.source, self.want)


def run(example):
    sio = StringIO.StringIO()
    if len(example.source.split('\n')) > 1:
        kind = 'exec'
    else:
        kind = 'single'
    
    try:
        code = compile(example.source, '<stdin>', kind)
        sys.stdout = sio
        exec code in globals()
        sys.stdout = stdout
        val = sio.getvalue().rstrip()
        
        if example.want != '' and val.find(example.want) < 0:
            return 'expected: "%s"\nactual:   "%s"' % (example.want, val)
    except Exception, se:
        if not example.want.find(str(se)):
            return 'expected: %s\nactual:   %s' % (example.want, val)
            
    return None
    

s = file(sys.argv[1]).read()

sys.stdin = StringIO.StringIO()

success = 0
failure = 0
linenum = 1
for mat in pat.finditer(s):
    code = mat.group(1)
    print 'code #%s' % linenum
    #print code
    linenum = linenum + 1
    examples = parse(code)
    for example in examples:
        response = run(example)
        if response:
            print 'exec: %s' % example.source
            print response
            failure = failure + 1
        else:
            success = success + 1

print '%s tests succeeded' % success
print '%s tests failed' % failure
