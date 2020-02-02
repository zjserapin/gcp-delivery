install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
test:
	#python -m pytest -vv  -vv --cov=myrepolib tests/*.pytest
	#python -m pytest --nbval notebook.ipynb

lint:
	pylint --disable=R,C main.py

all: install lint test