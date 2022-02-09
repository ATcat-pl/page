import requests
import os
from datetime import date
from flask import render_template, redirect, url_for, flash, request, Flask

app = Flask(__name__)


@app.route("/")
def home():
    return render("home.html")


@app.route('/pl/')
def pl_home_page():
    return render_template('pl/home.html')


@app.route('/en/')
def en_home_page():
    return render_template('en/home.html')


@app.route('/2s1b')
def MCserwer_page():
    return render_template('pl/2s1b.html')


@app.route('/about_us')
def about_us_page():
    return render('about_us_page.html')


@app.route('/help')
def help_page():
    return render('help.html')


@app.route('/my_yt_page')
def my_yt_page():
    return render_template('pl/mój_yt_1.html')


@app.route('/gra_win98')
def gra_win98():
    return render_template('pl/gra_win98.html')


@app.route('/program_downloads')
def program_downloads():
    return render('program_downloads.html')


@app.route('/program_downloads/gra_miasta')
def program_downloads_gra_miasta():
    return render("gra_miasta.html")


# tymczas
@app.route('/program_downloads/gra_miasta/test')
def program_downloads_gra_miasta_test():
    return render_template('pl/gra_miasta.html')


# /tymczas

@app.route('/program_downloads/gra_miasta/lastest_version')
def gra_miasta_version():
    response = requests.get("https://api.github.com/repos/Miasta-creators/Miasta_gra/releases/latest")
    return response.json()["name"]


@app.route('/program_downloads/gra_miasta/update_info')
def gra_miasta_update_info():
    return "texture+jar"  # texture+jar


@app.route('/atcatos')
def ATcatOS():
    return render_template('pl/atcat_os_home.html')


@app.route('/electronics/boards/ports-to-data-bus-series')
def PrtToDataBusBoardsSeries1():
    return render_template('unfinished.html')


def render(name):
    lang = str(request.accept_languages)
    language = lang.split(",")
    if (language[0] == "pl"):
        log("pl/" + name)
        return render_template("pl/" + name)
    else:
        log("en/" + name)
        return render_template("en/" + name)

def log(name):
    today = date.today()
    if os.path.isfile("log/" + today.strftime("%d-%m-%Y") + ".txt"):
        f = open("log/" + today.strftime("%d-%m-%Y") + ".txt", 'a')
    else:
        f = open("log/" + today.strftime("%d-%m-%Y") + ".txt", 'x')
    f.write("{\n")
    f.write("request: " + name + "\n")
    f.write("IP: " + str(request.remote_addr) + "\n")
    print(request.remote_addr)
    f.write("User-Agent: " + str(request.headers.get('User-Agent')) + "\n")
    print(request.headers.get('User-Agent'))
    f.write("Languages: " + str(request.accept_languages) + "\n")
    print(request.accept_languages)
    f.write("}\n")
    f.close()