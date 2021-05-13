from datetime import datetime
from flaskblog import db , login_manager
from flask_login import UserMixin

#Flask-Login은 Flask에 대한 사용자 세션관리를 제공
#오랜시간 동안 로그인, 로그아웃 및 사용자 세션 기억과 같은 작업을 처리


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # User과 post는 1:n 관계를 맺는다.
    # Relationship()은 User클래스 자체가 post클래스에 연결되어 있다는 사실을 알게해줌.
    # relationship()내에서 호출하는 backref는 역으로 클래스를 이용할 수 있도록
    # 즉 Post class에서 User class를 참조할수 있도록 Post.author를 구현

    # repr은 객체의 문자열을 반환한다, 객체의 자료형을 그대로 호출
    # f는 %s에 문자열 대입없이 중괄호 이용 다양한 표현식 사용가능
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
