from SAS.db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Schools(Base):

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    # Foreign key from district table
    district_id = Column(String, nullable = False)
    address = Column(String, nullable = False)
    subscription_status = Column(String, nullable = False)
    subscription_end_date = Column(String, nullable = False)