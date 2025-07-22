from flask import Flask, request, render_template, session
import random

app = Flask(__name__)
app.secret_key = 'gigigame'  # Needed for sessions

@app.route("/", methods=["GET", "POST"])
def home():
    if "number" not in session:
        session["number"] = random.randint(1, 10)
        session["count"] = 0

    message = ""

    if request.method == "POST":
        ip = request.form.get("guess")
        if ip and ip.isdigit():
            ip = int(ip)
            session["count"] += 1
            if ip == session["number"]:
                message = f"🎉 Correct! You guessed it in {session['count']} attempts."
                session.pop("number")
                session.pop("count")
            elif ip < session["number"]:
                message = "📉 Too low!"
            else:
                message = "📈 Too high!"
        else:
            message = "⚠️ Please enter a valid number."

    return render_template("index.html", message=message)
