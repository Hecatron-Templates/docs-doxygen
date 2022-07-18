# Readme

Copier template for project based documenation.
This template uses doxygen to generate xml files from source.  
The xml files are then parsed by spinx / [breathe](https://breathe.readthedocs.io/en/latest/) into markdown.  

This is the part of the docs that turns sourcecode into markdown.

## Usage

First enter / setup the python virtual environment
```sh
cd virtenv
# Under Linux
setup_venv.sh
# Under Windows
setup_venv.bat
```

TODO

## Requirements

  * doxygen needs to be installed and visible on the Path
    (under windows with would be C:\Program Files\doxygen\bin)
  * tox needs to be installed within python

```sh
pip install tox
```
