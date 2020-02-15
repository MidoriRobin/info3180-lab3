from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HalfBy50MasterdWins'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '6d9f81e0c479cf'
app.config['MAIL_PASSWORD'] = '78cd0f569796fd'
mail = Mail(app)
from app import views
