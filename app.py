import os

from flask import Flask, render_template, request
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
    return render_template("index.html", student_lst=student_lst, random_number = random.randint(0,1000),reverseName = reverseName)


app.run(
    port=int(os.getenv("PORT", "8080")),
    host=os.getenv("IP", "0.0.0.0")
)

