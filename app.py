import bcrypt
from Demos.win32ts_logoff_disconnected import username
from flask import *
from forms import registrationForm,loginForm
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
    model = UserModel()

    if login.validate_on_submit():
        uname = login.username.data
        pword = login.password.data
        nameresh = model.query.filter_by(username=uname).first()
        if bcrypt.checkpw(pword.encode('utf-8'),nameresh.password.encode('utf-8')) :
            flash('Login successful')
            return redirect('/Profile')
        else:
            flash('Login unsuccessful')
            return redirect('/Login')
    return render_template('login.html',title='Login',login=login)

@app.route('/Profile')
def profile():
    return render_template('profile.html',title='Profile')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
