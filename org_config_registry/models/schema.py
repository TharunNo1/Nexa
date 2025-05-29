from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from models.base import Base

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(String, unique=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)

    working_hours = Column(JSON)  # {"start": "09:00", "end": "18:00"}
    emergency_contacts = Column(JSON)  # list of phone numbers or emails
    locations = Column(JSON)  # [{"name": "BLR HQ", "geofence": [lat, lng]}]

    services = relationship("Service", back_populates="org", cascade="all, delete")


class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer, ForeignKey("organizations.id"))
    service_type = Column(String)
    endpoint_url = Column(String)
    eligible_agents = Column(JSON)  # e.g. ["hr_agent", "it_agent"]

    org = relationship("Organization", back_populates="services")