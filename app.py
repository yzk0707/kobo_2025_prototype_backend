from flask import Flask

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ルートURLにアクセスしたときの処理
@app.route('/')
def hello_world():
    return 'Hello from the Flask app in a container!'

@app.route('/register', methods=['POST'])
def register_team():
    # チーム登録処理を記述
    return 'Team registered successfully!'

# デバッグモードでの実行
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')