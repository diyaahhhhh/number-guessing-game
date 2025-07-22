from flask import Flask, request, render_template
import random

app = Flask(__name__)
number = random.randint(1, 10)
count = 0  # Starting attempts

@app.route("/", methods=["GET", "POST"])
def home():
    global number, count
    message = ""

    if request.method == "POST":
        ip = request.form.get("guess")
        if ip and ip.isdigit():
            ip = int(ip)
            if ip == number:
                message = f"🎉 Hurray! You guessed correctly in {count} attempts!"
                number = random.randint(1, 10)  # Reset for next round
                count = 0
            elif ip < number:
                message = "📉 Too low. Try again!"
                count += 1
            else:
                message = "📈 Too high. Try again!"
                count += 1
        else:
            message = "⚠️ Please enter a valid number!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
