from SAS.db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Videos(Base):

    id = Column(Integer, primary_key = True, index = True)
    youtube_link = Column(String, nullable = False)
    embed_code = Column(String, nullable = False)
    # User/Teacher_id Foreign key
    teacher_id = Column(Integer, nullable = False)
    approval_status = Column(String, nullable = False)
    # Class id from class table foreign key
    class_id = Column(Integer, nullable = False)