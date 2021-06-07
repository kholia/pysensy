make:
	python example.py

check:
	pylint example.py

test:
	pytest . -s
