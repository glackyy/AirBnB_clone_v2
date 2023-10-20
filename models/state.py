#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    if models.storage_t == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            var = models.storage.all()
            listarg = []
            res = []
            for k in var:
                city = k.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    listarg.append(var[k])
            for element in listarg:
                if (element.state_id == self.id):
                    res.append(element)
            return (res)
