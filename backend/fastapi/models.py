from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Show(Base):
    __tablename__ = "show_show"

    id = Column(Integer, primary_key=True, index=True)
    show_type = Column(String, index=True)
    title = Column(String, index=True)
    countries = Column(String, index=False)
    date_added = Column(String, index=False)
    rating = Column(String, index=False)
    duration = Column(String, index=False)
    categories = Column(String, index=False)
    description = Column(String, index=False)
    release_year = Column(Integer)

    director = relationship("Person", secondary = 'show_show_director', lazy='joined')
    cast = relationship("Person", secondary = 'show_show_cast', lazy='joined')


class Person(Base):
    __tablename__ = "show_person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Show_Director(Base):
    __tablename__ = 'show_show_director'

    show_id = Column (Integer, ForeignKey('show_show.id'), primary_key = True)
    person_id = Column (Integer, ForeignKey('show_person.id'), primary_key = True)


class Show_Cast(Base):
    __tablename__ = 'show_show_cast'

    show_id = Column (Integer, ForeignKey('show_show.id'), primary_key = True)
    person_id = Column (Integer, ForeignKey('show_person.id'), primary_key = True)

