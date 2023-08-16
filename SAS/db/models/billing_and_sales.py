from SAS.db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Billing_And_Sales(Base):

    id = Column(Integer, primary_key = True, index = True)
    # School id Foreign key
    school_id = Column(Integer, nullable = False)
    amount = Column(Integer, nullable = False)
    transaction_date = Column(String, nullable = False)
    subscription_type = Column(String, nullable = False)
    payment_gateway_reference = Column(String, nullable = False)