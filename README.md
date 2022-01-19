# UselessDjangoApp
This is a useless webapp (just for practice)

# Deploying Process
## Video Tutorial
[Click here to see the video](https://youtu.be/fH2S5lWNKaM "heroku deployment for django-sqlite3 app")

## Textual
1. At first [create account](https://www.heroku.com "heroku.com") or [login](https://id.heroku.com/login "heroku login") in heroku
1. Download `heroku-cli` from [here](https://cli-assets.heroku.com/heroku-x64.exe "click here") or [visit the website](https://devcenter.heroku.com/articles/heroku-cli#download-and-install "click here")

### 3. Create a virtual environment:
```terminal
pip install virtualenv
```
```terminal
virtualenv anyname
```
- After creating virtual environment activate your vitualenv
```terminal
pip install django gunicorn django-heroku
```

`You can run specific version like pip install django==2.2`

- Copy / Transfer your django-project in that virtual environment
- Add your dependencies to requirements.txt by typing in the terminal
```bash
pip freeze > requirements.txt
```

### 4. Setup your django-project before starting `heroku-deployment`
- Don't forget to add this in **settings.py**
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
```
- First, and most importantly, Heroku web applications require a `Procfile`

This file is used to explicitly declare your application’s process types and entry points. It is located in the root of your repository

#### Procfile
```
web: gunicorn yourprojectname.wsgi --log-file -
```
- Add the following `import` statement to the top of `settings.py`
```python
import django_heroku
```
- Then add the following to the bottom of `settings.py`
```python
# Activate Django-Heroku.
django_heroku.settings(locals())
```
- You can also made these changes in `settings.py`
```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*", "localhost"]
```

### 5. Final process of `heroku-deployment`
- **Open your terminal / cmd and run the following commands**
```bash
heroku login
```
- After run `heroku login` you can see this type of texts in your terminal
`
C:\Users\SUPRATIM\Desktop\UselessDjangoApp> heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/e1625921-dddc-400f-adc3-8f570d48ad0c?requestor=SFMyNTY.g2gDbQAAAAw0OS4zNy4zOS4yNTBuBgCYFdJzfgFiAAFRgA.enp9fW26_s1Hzn_VloGHmZpz3hi9QEY07WSUne6sOc4
Logging in... done
Logged in as supratimm531@gmail.com
`