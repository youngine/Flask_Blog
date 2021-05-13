from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# app객체 설정
# 어플리케이션의 시크릿키 추가
# SQLAlchemy 에서 사용할 데이터베이스의 위치 설정
# 설정 완료 했으면 SQLAlchemy 객체 생성
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# login process customizing
# 로그인하지 않은 유저가 login required 화면에 접근시
# 로그인 화면으로 redirect 해주는 기능
# 로그인 화면의 이름은 login_manager.login_view
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
