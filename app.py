import bcrypt
from flask import *
from forms import registrationForm,loginForm
from models import User ,db
from flask_login import LoginManager, current_user, login_user, logout_user,login_required

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modawana.db'
db.init_app(app)
app.secret_key = 'khairi'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.get('/')
@app.get('/Home')
def index():
    return render_template('index.html',title='Home')

@app.route('/Register', methods=['GET', 'POST'])
def register():
    #initialisate
    form = registrationForm()
    model = User()
    #validate
    if form.validate_on_submit():
        #get from the template
        uname = form.username.data
        pword = form.password.data
        #hash password
        pword_hash = bcrypt.hashpw(pword.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        model.username = uname
        model.password = pword_hash
        db.session.add(model)
        db.session.commit()
        flash('Registration successful')
        return redirect('/Login')
    return render_template("register.html", form=form,title='Register')


@app.route('/Login',methods=['GET','POST'])
def login():
    login = loginForm()
    model = User()

    if login.validate_on_submit():
        uname = login.username.data
        pword = login.password.data
        nameresh = model.query.filter_by(username=uname).first()
        if bcrypt.checkpw(pword.encode('utf-8'),nameresh.password.encode('utf-8')) :
            login_user(nameresh)
            flash('Login successful')
            return redirect('/Profile')
        else:
            flash('Login unsuccessful')
            return redirect('/Login')
    return render_template('login.html',title='Login',login=login)

@app.route('/Profile',methods=['GET','POST'])
@login_required
def profile():
    return render_template('profile.html',title='Profile')


@app.route('/Logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful')
    return redirect(url_for('login'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
