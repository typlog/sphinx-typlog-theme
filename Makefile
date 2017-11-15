.PHONY: docs

docs:
	@rm -fr docs/_build
	@$(MAKE) -C docs html
