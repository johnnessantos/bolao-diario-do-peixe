install:
	@pip install -r requirements.txt

run:
	@gunicorn wsgi:app --bind localhost:8080 --reload

deploy:
	git push heroku master
