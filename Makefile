.PHONY: docs css

docs:
	@rm -fr docs/_build
	@$(MAKE) -C docs html
