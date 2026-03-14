from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>UT Bot is Online!</h1>"

if __name__ == "__main__":
    # ده البورت اللي موقع Render بيفهمه
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
