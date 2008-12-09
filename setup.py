from distutils.core import setup, Command
from distutils.spawn import find_executable, spawn
from zipfile import ZipFile

import os
import re


#
# where to write target files
#
target_dir = 'target'

#
# 'root' tex files for each OS
#
sources = 'swfk-mac', 'swfk-linux', 'swfk-win'
#sources = 'swfk-linux',

#
# find the executables to use in compiling the books
#
latex = find_executable('latex')
makeindex = find_executable('makeindex')
dvipdf = find_executable('dvipdf')

#
# Get the book version
#
s = open('frontmatter.tex').read()
mat = re.compile(r'Version\s*(.*)').search(s)
version = mat.group(1)


class CleanCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        self._clean_me = [ ]
        for root, dirs, files in os.walk(target_dir):
            for f in files:
                self._clean_me.append(os.path.join(root, f))

    def finalize_options(self):
        pass

    def run(self):
        for clean_me in self._clean_me:
            try:
                os.unlink(clean_me)
            except:
                pass


class LatexCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for src in sources:
            tex = '%s.tex' % src
            spawn([latex, '--output-directory=%s' % target_dir, tex])

            spawn([makeindex, '%s/%s.idx' % (target_dir, src)])
            spawn([latex, '--output-directory=%s' % target_dir, tex])

            pdf = '%s/%s-%s.pdf' % (target_dir, src, version)
            spawn([dvipdf, '%s/%s.dvi' % (target_dir, src), pdf])

            zf = ZipFile('%s/%s.zip' % (target_dir, src), 'w')
            zf.write(pdf)
            zf.close()


setup(
    name = 'SWFK',
    version = '1.00',
    description = 'Snake Wrangling For Kids',

    author = 'Jason R Briggs',
    author_email =  'jason@briggs.net.nz',

    cmdclass = { 'clean': CleanCommand, 'build' : LatexCommand }

)
