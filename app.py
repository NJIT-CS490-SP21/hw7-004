import os
from flask import Flask, render_template

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route("/")
def index():
    return render_template("index.html")

app.run(
    port=int(os.getenv("PORT", "8080")),
    host=os.getenv("IP", "0.0.0.0")
)

