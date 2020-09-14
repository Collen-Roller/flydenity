include .env

tag:
	git tag -a v${VERSION} -m "version ${VERSION} release"
	git push origin --tags

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf dist/

release: clean
	python3 setup.py sdist bdist_wheel
	twine upload --repository pypi dist/*

install: clean
	pip3 install -r requirements.txt
	pip3 install .
