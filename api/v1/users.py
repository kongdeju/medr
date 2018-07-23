
from sqlalchemy import Column,Integer,String
from db import Base
from db import engine
from sqlalchemy.orm import sessionmaker
from flask import request
from flask_restful import Resource
Session = sessionmaker(bind=engine)
import json


class User(Base):
    __tablename__ = "user"

    id = Column("id",Integer,primary_key=True)
    username = Column("username",String,unique=True)



class Users_(Resource):

    def get(self):
        session = Session()
        users = session.query(User).all()
        session.close()
        return users

    def post(self):
        session = Session()
        auser = User(id=5,username="deju")
        session.add(auser)
        session.commit()

