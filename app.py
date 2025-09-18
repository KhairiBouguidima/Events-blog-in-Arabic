import hashlib

import bcrypt
from argon2 import hash_password
from fastapi_users import password
from flask import *
from forms import registrationForm
from flask_login import LoginManager, UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from models import UserModel ,db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modawana.db'
db.init_app(app)
app.secret_key = 'khairi'

@app.get('/')
@app.get('/Home')
def index():
    return render_template('index.html',title='Home')

@app.route('/Register', methods=['GET', 'POST'])
def register():
    #initialisate
    form = registrationForm()
    model = UserModel()
    #validate
    if form.validate_on_submit():
        #get from the template
        uname = form.username.data
        pword = form.password.data
        #hash password
        pword_hash = bcrypt.hashpw(pword.encode('utf-8'), bcrypt.gensalt())

        model.username = uname
        model.password = pword_hash
        db.session.add(model)
        db.session.commit()
        flash('Registration successful')
        return redirect('/Register')
    return render_template("register.html", form=form,title='Register')


@app.get('/Login')
def login():
    return render_template('login.html',title='Login')



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
