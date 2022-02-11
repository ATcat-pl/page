import datetime
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import flask
import requests
import os
from datetime import date, timedelta
from flask import render_template, redirect, url_for, flash, request, Flask

app = Flask(__name__)
# app.config['SECRET_KEY'] = "edrftghyujikmlo,ikujhygtrf"

log_ = True
banned_user_agents = ["Go-http-client/1.1"]
banned_ip = []

active_users = []

@app.route("/")
def home():
    return render("home.html")


@app.route('/pl/')
def pl_home_page():
    log('pl/home.html')
    return render_template('pl/home.html')


@app.route('/en/')
def en_home_page():
    log('en/home.html')
    return render_template('en/home.html')


@app.route('/2s1b')
def MCserwer_page():
    log('pl/2s1b.html')
    return render_template('pl/2s1b.html')


@app.route('/about_us')
def about_us_page():
    return render('about_us_page.html')


@app.route('/help')
def help_page():
    return render('help.html')


@app.route('/my_yt_page')
def my_yt_page():
    log('pl/mój_yt_1.html')
    return render_template('pl/mój_yt_1.html')


@app.route('/gra_win98')
def gra_win98():
    log('pl/gra_win98.html')
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
    log('pl/gra_miasta.html')
    return render_template('pl/gra_miasta.html')


# /tymczas

@app.route('/program_downloads/gra_miasta/lastest_version')
def gra_miasta_version():
    log("Null")
    response = requests.get("https://api.github.com/repos/Miasta-creators/Miasta_gra/releases/latest")
    return response.json()["name"]


@app.route('/program_downloads/gra_miasta/update_info')
def gra_miasta_update_info():
    log("Null")
    return "texture+jar"  # texture+jar


@app.route('/atcatos')
def ATcatOS():
    log('pl/atcat_os_home.html')
    return render_template('pl/atcat_os_home.html')


@app.route('/electronics/boards/ports-to-data-bus-series')
def PrtToDataBusBoardsSeries1():
    log("Null")
    return render_template('unfinished.html')

@app.route('/program_downloads/gra_miasta/user_auth', methods=["GET", "POST"])
def game_user_auth():
    today = date.today()

    try:
        userId = str(request.headers.get('UserId'))
        userPassword = str(request.headers.get('UserPassword'))
        goodPassword = os.environ['loginPassword']
    except:
        return flask.Response(status=400)

    if log_:
        if os.path.isfile("log/" + today.strftime("%d-%m-%Y") + ".txt"):
            f = open("log/" + today.strftime("%d-%m-%Y") + ".txt", 'a')
        else:
            f = open("log/" + today.strftime("%d-%m-%Y") + ".txt", 'x')
        t = time.localtime()
        f.write(
            "{\nTime: " + f"{t.tm_hour}:{t.tm_min}:{t.tm_sec} \n" + "Request: " + request.path + f", userId: {userId}" "\nSecure: " + str(
                bool(request.is_secure)) + "\nIP: " + str(request.remote_addr) + "\nTransmission method: " + str(
                request.method) + "\nScheme: " + request.scheme + "\nUser-Agent: " + str(
                request.headers.get('User-Agent')) + "\n")

    if request.method == 'GET':
        if userPassword == goodPassword:
            if userId not in active_users:
                active_users.append(userId)
                print(f"User {userId} tried to log in returned: OK")
                if log_:
                    f.write("returned: OK\n}\n")
                    f.close()
                return "OK"
            else:
                print(f"User {userId} tried to log in returned: User in use")
                if log_:
                    f.write("returned: User in use\n}\n")
                    f.close()
                return f"User in use"
        else:
            if log_:
                f.write("returned: Bad password\n}\n")
                f.close()
            return "Bad password"
    elif request.method == 'POST':
        if userPassword == goodPassword:
            if userId in active_users:
                print(f"User {userId} logged off")
                active_users.remove(userId)
                if log_:
                    f.write("returned: status_code{200}\n}\n")
                    f.close()

                return flask.Response(status=200)
            else:
                if log_:
                    f.write("returned: status_code{401}\n}\n")
                    f.close()
                return flask.Response(status=401)
        else:
            if log_:
                f.write("returned: Bad password (status_code{423})\n}\n")
                f.close()
            return flask.Response(status=423)
    else:
        if log_:
            f.write("returned: status_code{400}\n}\n")
            f.close()
        return flask.Response(status=400)

def render(name):
    if str(request.headers.get('User-Agent')) not in banned_user_agents and str(request.remote_addr) not in banned_ip:
        lang = str(request.accept_languages)
        language = lang.split(",")
        ip = str(request.remote_addr)
        if (language[0] == "pl"):
            log("pl/" + name)
            # return render_template("pl/" + name, ip="   Twoje IP: "+ip, log_=log_)
            return render_template("pl/" + name, ip=" ", log_=log_)
        else:
            log("en/" + name)
            # return render_template("en/" + name, ip="   Your IP: "+ip, log_=log_)
            return render_template("en/" + name, ip=" ", log_=log_)
    else:
        return flask.Response(status=403)

def log(name):
    today = date.today()
    if log_:
        if "UptimeRobot" not in str(request.headers.get('User-Agent')):
            if os.path.isfile("log/" + today.strftime("%d-%m-%Y") + ".txt"):
                f = open("log/" + today.strftime("%d-%m-%Y") + ".txt", 'a+b')
            else:
                f = open("log/" + today.strftime("%d-%m-%Y") + ".txt", 'x+b')
            t = time.localtime()

            # ip = request.remote_addr
            # while len(ip) % 16 != 0:
            #     ip = ip + ' '
            bytestowrite = bytes("{\nTime: "+ f"{t.tm_hour}:{t.tm_min}:{t.tm_sec} \n" + "Request: " + request.full_path + ", file: " + name + "\nSecure: "+str(bool(request.is_secure))+"\nIP", "UTF-8")
            f.write(bytestowrite)
            # cipher = Cipher(algorithms.AES(bytes(os.environ['AES_key'], "UTF-8")), modes.CBC(bytes(os.environ['CBC_key'], "UTF-8")))
            # encryptor = cipher.encryptor()
            # encrypted = encryptor.update(bytes(ip, "UTF-8")) + encryptor.finalize()
            # f.write(bytes(" (encrypted): +encrypted.hex(), "UTF-8"))
            # !!!
            # wyłączone bo wyśiwetla wewnętrzne ip w sieci i jeśli jest z zewnątrz to pokazuje ip routera
            # !!!
            # wyłączone jest w funkcjach: render(), log()
            f.write(bytes(": - ", "UTF-8"))
            bytestowrite = bytes("\nTransmission method: "+ str(request.method) + "\nScheme: " + request.scheme + "\nUser-Agent: " + str(request.headers.get('User-Agent')) + "\n" + "Languages: " + str(request.accept_languages) + "\n" + "}\n", "UTF-8")
            f.write(bytestowrite)
            f.close()
    print(request.remote_addr)
    print(request.headers.get('User-Agent'))
    print(request.accept_languages)

    old = today - timedelta(days=3)
    if os.path.isfile("log/"+old.strftime("%d-%m-%Y")+".txt"):
        os.remove("log/"+old.strftime("%d-%m-%Y")+".txt")
        print("removed: log/"+old.strftime("%d-%m-%Y")+".txt")
