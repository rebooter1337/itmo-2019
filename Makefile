SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run flake8 .

.PHONY: unit
unit:


.PHONY: typecheck
typecheck:
	poetry run sh bin/typecheck.sh

.PHONY: package
package:
	poetry check
	poetry run pip check

.PHONY: test
test: lint typecheck unit package
