from SAS.db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Content_Policies(Base):

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    detais = Column(String, nullable = False)
    # Admin/Teacher_id Foreign key
    teacher_id = Column(Integer, nullable = False)
    # School id Foreign key
    school_id = Column(Integer, nullable = False)