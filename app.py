import datetime
import time

import requests
import os
from datetime import date, timedelta
from flask import render_template, redirect, url_for, flash, request, Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "edrftghyujikmlo,ikujhygtrf"

@app.route("/")
def home():
    return render("home.html", "/")


@app.route('/pl/')
def pl_home_page():
    log('pl/home.html', '/pl/')
    return render_template('pl/home.html')


@app.route('/en/')
def en_home_page():
    log('en/home.html', '/en/')
    return render_template('en/home.html')


@app.route('/2s1b')
def MCserwer_page():
    log('pl/2s1b.html', '/2s1b')
    return render_template('pl/2s1b.html')


@app.route('/about_us')
def about_us_page():
    return render('about_us_page.html', '/about_us')


@app.route('/help')
def help_page():
    return render('help.html', '/help')


@app.route('/my_yt_page')
def my_yt_page():
    log('pl/mój_yt_1.html', '/my_yt_page')
    return render_template('pl/mój_yt_1.html')


@app.route('/gra_win98')
def gra_win98():
    log('pl/gra_win98.html', '/gra_win98')
    return render_template('pl/gra_win98.html')


@app.route('/program_downloads')
def program_downloads():
    return render('program_downloads.html', '/program_downloads')


@app.route('/program_downloads/gra_miasta')
def program_downloads_gra_miasta():
    return render("gra_miasta.html", '/program_downloads/gra_miasta')


# tymczas
@app.route('/program_downloads/gra_miasta/test')
def program_downloads_gra_miasta_test():
    log('pl/gra_miasta.html', '/program_downloads/gra_miasta/test')
    return render_template('pl/gra_miasta.html')


# /tymczas

@app.route('/program_downloads/gra_miasta/lastest_version')
def gra_miasta_version():
    log("Null", '/program_downloads/gra_miasta/lastest_version')
    response = requests.get("https://api.github.com/repos/Miasta-creators/Miasta_gra/releases/latest")
    return response.json()["name"]


@app.route('/program_downloads/gra_miasta/update_info')
def gra_miasta_update_info():
    log("Null", '/program_downloads/gra_miasta/update_info')
    return "texture+jar"  # texture+jar


@app.route('/atcatos')
def ATcatOS():
    log('pl/atcat_os_home.html', '/atcatos')
    return render_template('pl/atcat_os_home.html')


@app.route('/electronics/boards/ports-to-data-bus-series')
def PrtToDataBusBoardsSeries1():
    log("Null", '/electronics/boards/ports-to-data-bus-series')
    return render_template('unfinished.html')


def render(name, path):
    lang = str(request.accept_languages)
    language = lang.split(",")
    if (language[0] == "pl"):
        log("pl/" + name, path)
        return render_template("pl/" + name)
    else:
        log("en/" + name, path)
        return render_template("en/" + name)


def log(name, path):
    today = date.today()
    if "UptimeRobot" not in str(request.headers.get('User-Agent')):
        if os.path.isfile("log/" + today.strftime("%d-%m-%Y") + ".txt"):
            f = open("log/" + today.strftime("%d-%m-%Y") + ".txt", 'a')
        else:
            f = open("log/" + today.strftime("%d-%m-%Y") + ".txt", 'x')
        t = time.localtime()
        f.write("{\nTime: "+ f"{t.tm_hour}:{t.tm_min}:{t.tm_sec} \n" + "Request: " + path + ", file: " + name + "\n" + "IP: " + str(request.remote_addr) + "\n" + "User-Agent: " + str(request.headers.get('User-Agent')) + "\n" + "Languages: " + str(request.accept_languages) + "\n" + "}\n")
        f.close()
    print(request.remote_addr)
    print(request.headers.get('User-Agent'))
    print(request.accept_languages)

    old = today - timedelta(days=10)
    if os.path.isfile("log/"+old.strftime("%d-%m-%Y")+".txt"):
        os.remove("log/"+old.strftime("%d-%m-%Y")+".txt")
        print("removed: log/"+old.strftime("%d-%m-%Y")+".txt")
