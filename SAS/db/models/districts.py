from SAS.db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Districts(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    # Foreign key from users/admin table
    admin_id = Column(Integer, nullable=False)