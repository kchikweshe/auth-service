from datetime import datetime

from sqlalchemy.orm import relationship

import database
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

Base = database.Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    email = Column(String(20))
    password = Column(String(160))
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")
