import os
from flask import Flask, render_template
import random

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route("/")
def index():
    return render_template(
        "index.html",
        random_number = random.randint(0,1000)
    )

app.run(
    port=int(os.getenv("PORT", "8080")),
    host=os.getenv("IP", "0.0.0.0")
)

