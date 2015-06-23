#! /usr/bin/env python

import os
import re
import sys
from io import StringIO

pat = re.compile(r'\\begin{listing}\s*\\begin{verbatim}\s*(.*?)\\end{verbatim}', re.DOTALL | re.MULTILINE)
split_re = re.compile(r'\s*')
line_re = re.compile(r'^\s*[0-9]+\.\s*')

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
        line = line_re.sub('', line)
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

def percent_match(tokenlist, str):
    count = 0
    for token in tokenlist:
        if str.find(token) >= 0: 
            count += 1
    return (count / len(tokenlist))


def run(example):
    sio = StringIO()
    if len(example.source.split('\n')) > 1:
        kind = 'exec'
    else:
        kind = 'single'
    
    l = []
    sys.stdout = sio
    try:
        code = compile(example.source, '<stdin>', kind)
        exec(code, globals())
        val = sio.getvalue().rstrip()
        if example.want != '' and val.find(example.want) < 0:
            return 'expected: "%s"\nactual:   "%s"' % (example.want, val)
    except Exception as se:
        sys.stdout = stdout
        err = str(se)
        tokens = split_re.split(err[0:err.find('(')])
        match = percent_match(tokens, example.want)
        if match < 0.7:
            return 'expected: %s\nactual:   %s\n(%% match = %s)' % (example.want, str(se), match)
    finally:
        sys.stdout = stdout

    return None
    

s = open(sys.argv[1]).read()

sys.stdin = StringIO()

success = 0
failure = 0
linenum = 1
for mat in pat.finditer(s):
    code = mat.group(1)
    print('\n\ncode #%s' % linenum)
    linenum = linenum + 1
    examples = parse(code)
    for example in examples:
        response = run(example)
        if response:
            print('exec:\n%s' % example.source)
            print(response)
            failure = failure + 1
        else:
            success = success + 1

print('%s tests succeeded' % success)
print('%s tests failed' % failure)
