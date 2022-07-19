# Usage

## Setup a virtual python environment with all the needed tools installed

First enter / setup the python virtual environment
```sh
cd virtenv
# Under Linux
setup_venv.sh
# Under Windows
setup_venv.bat
```

## Doxygen

The first stage is the running of Doxygen.  
This parses the sourcecode and outputs the result as xml into the xml-build sub directory.  
If you look at the differences in the configuration between Doxyfile and Doxyfile.default  
The main two to watch out for are PROJECT_NAME and INPUT which may change based on the project name.

## Breathe

The next stage is the running of breathe, this is an extension to the sphinx static site generator.  
What we do here is generate the html and then extract it for use later on
