import sys
from os import path
from sphinx.cmd.build import main

# Get a directory path relative to this script
def get_path(dirpath):
    scriptdir = path.dirname(__file__)
    destpath = path.join(scriptdir, dirpath)
    destpath = path.abspath(destpath)
    return destpath

# Setup sphinx options
# https://www.sphinx-doc.org/en/master/man/sphinx-build.html
opts = []

# Set for outputing to markdown
opts += ['-b', 'markdown']

# Set the cache directory to outside the build directory
doctreesdir = get_path('doctrees')
opts += ['-d', doctreesdir]

# Pull conf.py from here instead of the source directory
confpath = get_path('.')
opts += ['-c', confpath]

# Specify source and destination
srcdir = get_path('source')
builddir = get_path('build')
opts += [srcdir, builddir]

# Run Spinx
#sys.exit(main(sys.argv[1:]))
sys.exit(main(opts))
