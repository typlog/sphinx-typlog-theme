.PHONY: docs

docs:
	@rm -fr docs/_build
	@$(MAKE) -C docs html


clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg
	@rm -fr *.egg-info


clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +


install:
	@pip install -e '.[dev]'
	@npm install

serve:
	@npm run build
	@make docs
	@python server.py
