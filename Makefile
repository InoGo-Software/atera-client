build:
	docker build . -t atera-api

black:
	docker run -v `pwd`/:/code atera-api bash -c "black atera_client -l 120"

publish:
	docker run -e TWINE_USERNAME=${TWINE_USERNAME} -e TWINE_PASSWORD=${TWINE_PASSWORD} atera-api bash -c "python3 setup.py sdist bdist_wheel && twine upload --verbose --skip-existing dist/*"