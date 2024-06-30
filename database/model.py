from sqlalchemy import Column, Integer, String, DateTime
from database.database_handler import Base

class Passwords(Base):
    __tablename__ = 'passwords'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    account_name = Column(String, nullable=False)
    website_url = Column(String, nullable=False)
    password = Column(String, nullable=False)
    notes = Column(String)
    created_at = Column(DateTime, nullable=False)