define HELPBODY
Available commands:

	make help       - this thing.

	make build      - build for package
	make clean      - clean build and pyc

endef

export HELPBODY
help:
	@echo "$$HELPBODY"

build:
	python setup.py install

develop:
	python setup.py develop

clean:
	rm -rf dist build aioethereum.egg-info aioethereum/*.pyc *.pyc .cache .tox .coverage coverage.*

upload_test:
	python setup.py sdist bdist_wheel upload -r pypitest

upload:
	python setup.py sdist bdist_wheel upload -r pypi