Shorten Link Project

1. Features
	- Full webapp that allow user to shorten their links into 6-character-long links.

	- Authentication and Permission Features using django allauth: user that login can store and view their links after being shortened.

2. Data model
	- Link:
		+ user
		+ link_web
		+ shortlink
		+ status
		+ timestamp

Setup Project:

1. virtualenv venv

2. pip install -r requirements.txt

3. python manage.py runserver

In admin site:

username: amin
password: Minh1234