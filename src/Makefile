docker=docker run -it --rm \
 -e SLACK_WEBHOOK_URL="$(SLACK_WEBHOOK_URL)" \
 -p 8000:8000 \
 -v $(PWD)/db.sqlite3:/usr/src/app/db.sqlite3 \
 --name back-django back-django-build

run: migrate
	$(docker)

test: migrate
	$(docker) python3 manage.py test -v 2

build:
	docker build -t back-django-build .

migrate: db.sqlite3 build
	$(docker) python3 manage.py migrate

createsuperuser: migrate
	$(docker) python manage.py createsuperuser

db.sqlite3:
	touch db.sqlite3

coverage: test
	pytest
