.PHONY: validate test build check links stats

validate:
	python3 scripts/validate.py

test:
	python3 -m unittest discover -s tests -v

build:
	python3 scripts/build_readme.py

# everything CI runs, in one command
check: validate test
	python3 scripts/build_readme.py --check

links:
	python3 scripts/check_links.py

stats:
	python3 scripts/query.py stats
