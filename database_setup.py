import os
import sysconfig
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    provider = Column(String(250))

class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    img = Column(String(250), nullable = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }

class CategoryItem(Base):
    __tablename__ = 'category_item'

    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(500))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship(Categories)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,

        }

engine = create_engine('sqlite:///itemcatalog.db')
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)