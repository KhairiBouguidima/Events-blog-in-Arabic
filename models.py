from flask_login import current_user , login_required,UserMixin
from flask_sqlalchemy import SQLAlchemy ,model
from sqlalchemy import String, ForeignKeyConstraint
from sqlalchemy.orm import mapped_column,Mapped ,DeclarativeBase
db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id:Mapped[int] = mapped_column(db.Integer, primary_key=True ,autoincrement=True)
    username :Mapped[str] = mapped_column(db.String)
    password:Mapped[str] = mapped_column(db.String)

#class publicationModel (db.Model):
   # __tablename__ = 'publication'
    #id:Mapped[int] = mapped_column(db.Integer, primary_key=True )
    #title:Mapped[str] = mapped_column(db.String)
    #description:Mapped[str] = mapped_column(db.String)
    #__table_args__ = (ForeignKeyConstraint(['id'],['UserModel.id']),)


