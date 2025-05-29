from typing import Optional, List, Dict, Any
from pydantic import BaseModel

class ServiceCreate(BaseModel):
    service_type: str
    endpoint_url: str
    eligible_agents: List[str]

class OrgCreate(BaseModel):
    org_id: str
    name: str
    description: Optional[str] = None
    working_hours: Optional[Dict[str, str]] = None  
    emergency_contacts: Optional[List[str]] = None
    locations: Optional[List[Dict[str, Any]]] = None
    services: Optional[List[ServiceCreate]] = []

class OrgResponse(OrgCreate):
    id: int
    services: List[ServiceCreate]
