#!/bin/python3
python3 -m venv venv
source venv/bin/activate 
pip install --upgrade pip
pip install pipreqs
pipreqs . --force
pip install -r requirements.txt 
