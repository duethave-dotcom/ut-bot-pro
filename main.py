import os
from flask import Flask

app = Flask(__name__)

# هنا بنخلي السيرفر يستقبل البيانات اللي العميل هيدخلها
@app.route('/')
def home():
    return """
    <h1>MetaTrader 5 Bot System</h1>
    <p>Status: <b>Online & Live</b></p>
    <p>Waiting for MT5 Configuration...</p>
    """

if __name__ == "__main__":
    # ده البورت اللي Render بيشغله
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
