from flask import Flask
from .models import db, Team # models.pyからdbとTeamをインポート
from .api import api_bp # api.pyからブループリントをインポート

def create_app():
    app = Flask(__name__)
    
    # データベース設定 (今回はSQLiteを使用)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # データベースとアプリケーションを紐付け
    db.init_app(app)
    
    # ブループリントを登録
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # アプリケーションコンテキスト内でテーブルを作成
    with app.app_context():
        db.create_all()
    
    return app