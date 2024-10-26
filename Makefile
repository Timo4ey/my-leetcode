black:
	poetry run black .

pep-isort:
	poetry run isort .

my-test:
	pytest test/__init__.py 