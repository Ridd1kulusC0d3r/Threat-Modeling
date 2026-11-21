.PHONY: validate test build check links stats lab ingest

validate:
	python3 scripts/validate.py

test:
	python3 -m unittest discover -s tests -v

build:
	python3 scripts/build_readme.py

# everything CI runs, in one command
check: validate test lab
	python3 scripts/build_readme.py --check

links:
	python3 scripts/check_links.py

stats:
	python3 scripts/query.py stats

# run detection rules against the synthetic fixtures in lab/
lab:
	python3 scripts/lab.py run

# suggest candidates from the feeds repo OPML (report only): make ingest OPML=../feeds/feeds.opml
ingest:
	python3 scripts/ingest_feeds.py $(OPML)
