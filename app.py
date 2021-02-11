import os

from flask import Flask, render_template, request
import requests
import random


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
global student_lst
student_lst = []

@app.route("/", methods=['POST', 'GET'])
def index():

    global student_lst
    reverseName = ''
    if request.method == 'POST' and "student_btn" in request.form:
        student = request.form['student']
        student_lst.append(student)
        reverseName = student[::-1].lower()

    try:
        ifconfig = requests.get('http://ifconfig.co/json').json()
    except Exception as e:
        print(e)
        ifconfig = False
        # do nothing with it though

    return render_template("index.html", student_lst=student_lst, random_number=random.randint(0, 1000), reverseName=reverseName, ifconfig=ifconfig)


app.run(
    port=int(os.getenv("PORT", "8080")),
    host=os.getenv("IP", "0.0.0.0")
)

