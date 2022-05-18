#!/bin/bash
# Usage:
# source init_script.sh

if [ ! -d "pyvenv" ]; then

	echo "Virtual Environment not found. Creating .."
	#virtualenv pyvenv           # Python2.7
	python3 -m venv pyvenv     # Python3.6
	source pyvenv/bin/activate

	if [ $VIRTUAL_ENV != "" ]; then
	 echo "Virtual Env Activated"
	 pip install -r src/requirements.txt
	fi

fi

