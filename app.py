from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# List of quotes
quotes = [
    "Keep going, you're doing great!",
    "Failure is the opportunity to begin again.",
    "Believe in yourself and all that you are.",
    "The only limit is the one you set yourself.",
    "Success is not final; failure is not fatal."
]

@app.route("/")
def home():
    random_quote = random.choice(quotes)
    return render_template("index.html", quote=random_quote)

if __name__ == '__main__':
    # Render uses the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)  # Bind to 0.0.0.0 and use the correct port

