# Readme

Copier template for project based documenation.
This template uses doxygen to generate xml files from source.  
The xml files are then parsed by spinx / [breathe](https://breathe.readthedocs.io/en/latest/) into html.  

This can then be extracted for use with other static site generators (such as docusaurus).  
One of the advantages docusaurus has over sphinx is that it's an SPA so the pages load quicker.

## Other options

Some of the other options for converting doxygen XML to markdown include

  * https://github.com/vstakhov/doxydown
  * https://github.com/pferdinand/doxygen2md
  * https://github.com/sourcey/moxygen
  * https://github.com/matusnovak/doxybook2
  * https://github.com/matusnovak/doxybook

However they don't seem to have gotten as much attention as breathe

  * https://github.com/michaeljones/breathe
  * https://pypi.org/project/exhale/

As far as integration with static site generators other than Sphinx there's some more info here.

  * https://github.com/facebook/docusaurus/issues/1059
  * https://github.com/pytorch/botorch/blob/main/scripts/build_docs.sh

