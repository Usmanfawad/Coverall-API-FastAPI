from SAS.db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Notifications_And_Alerts(Base):

    id = Column(Integer, primary_key = True, index = True)
    # User id Foreign key
    user_id = Column(Integer, nullable = False)
    notification_text = Column(String, nullable = False)
    status = Column(String, nullable = False)
    timestamp = Column(String, nullable = False)