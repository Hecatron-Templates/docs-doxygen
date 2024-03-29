#! /bin/bash

if [ -z "$1" ]
then
      venv=$1
else
      venv="pydev-env"
fi

if [ ! -d "./$venv" ]; then
  echo "Creating virtual environment $venv"
  tox -c tox.ini
  source $venv/bin/activate
fi

# Enter the python virtual enviro on the current shell
echo "Entering virtual environment $venv"
bash --rcfile <(echo '. ./pydev-env/Scripts/activate')

# use echo $BASHPID to check the bash prompt process id
