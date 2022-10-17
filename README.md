# **Rest-Api-Game-Gunting-Kertas-Batu**
<p align="center">
<img src="https://avatars.githubusercontent.com/Xenzi-XN1" width="200" height="200"/>
</p>
<p align="center">
  <a href="#"><img src="http://readme-typing-svg.herokuapp.com?color=d1fa02&center=true&vCenter=true&multiline=false&lines=Welcome+To+Rest-Api-Game-Gunting-Kertas-Batu" alt="">
</p>
<p align="center">
<a href="https://github.com/Xenzi-XN1"><img title="Creator" src="https://img.shields.io/badge/Creator-Xenzi-green.svg?style=for-the-badge&logo=github"></a>
</p>
Simple Rest-API Rest-Api-Game-Gunting-Kertas-Batu menggunakan flask

## Cloning this repo
```cmd
> git clone https://github.com/Aldi098/Rest-Api-Game-Gunting-Kertas-Batu
> cd Rest-Api-Game-Gunting-Kertas-Batu
```

## Run Rest-API
```cmd
> pip install -r requirements.txt
> python run.py
```

<img src="https://i.ibb.co/HqK1FbQ/IMG-20220902-154034.jpg" width="500">

# Tutorial
Rest-API User-agent-Random ini menggunakan metode `POST`
```cmd
http://127.0.0.1:5000/api/game/batu-gunting-kertas
```

Menggunakan `python`
```python
import requests
res = requests.post('http://127.0.0.1:5000/game/batu-gunting-kertas', data={"user":"nama mu","poin":"100","game":"batu"}).text
print (res)
```
# Contoh game yang saya buat, source code ada di folder Rest-Api-Game-Gunting-Kertas-Batu/src

<img src="https://i.ibb.co/HqK1FbQ/IMG-20220902-154034.jpg" width="500">

# Deploy Heroku

Go to [Heroku](https://heroku.com) and Login

Create New App ( App Name For Example : abcd-api)

<img src="https://i.postimg.cc/Z5T8Btw2/newapp.png" width="500">

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

Open `CMD` and Login Heroku

```cmd
> heroku login
```

Initialize a git repository in a new or existing directory

```cmd
> cd Rest-Api-Game-Gunting-Kertas-Batu
> git init
```

Remote Your App, Use `heroku git:remote -a app-name`

```cmd
> heroku git:remote -a abcd-api
```

Commit your code to the repository and deploy it to Heroku using Git.

```cmd
> git add .
> git commit -am "make it better"
> git push heroku master
```

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/)
