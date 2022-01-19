# UselessDjangoApp
This is a useless webapp (just for practice)

# Deploying Process
## Video Tutorial
[Click here to see the video](https://youtu.be/fH2S5lWNKaM "heroku deployment for django-sqlite3 app")

## Textual
1. At first [create account](https://www.heroku.com "heroku.com") or [login](https://id.heroku.com/login "heroku login") in heroku
1. Download `heroku-cli` from [here](https://cli-assets.heroku.com/heroku-x64.exe "click here") or [visit the website](https://devcenter.heroku.com/articles/heroku-cli#download-and-install "click here")

- **Create a virtual environment:**
```
$ pip install virtualenv
```
```
$ virtualenv anyname
```
- After creating virtual environment activate your vitualenv
```
$ pip install django gunicorn django-heroku
```