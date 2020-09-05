from sqlalchemy import Column, Integer, String, Table, DateTime, Date, text
from sqlalchemy.sql import func
from ..database import Base


class user_table(Base):
    __tablename__ = "user_table"
    user_id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String(255), nullable=False)
    gender = Column(String(11), nullable=True)
    email = Column(String(255), nullable=True)
    password = Column(String(500), nullable=True)
    phone_no = Column(String(11), nullable=True)
    login_type = Column(String(10), nullable=False)
    dob = Column(Date, nullable=True)
    google_id = Column(String(255), nullable=True)
    facebook_id = Column(String(255), nullable=True)
    created_on = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    modified_on = Column(DateTime(timezone=True),
                         onupdate=func.now(), nullable=True)
