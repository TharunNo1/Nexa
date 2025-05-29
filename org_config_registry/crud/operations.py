from sqlalchemy.orm import Session
from models.schema import Organization, Service
from schemas.pydantic_models import OrgCreate

def create_organization(db: Session, org: OrgCreate):
    db_org = Organization(
        org_id=org.org_id,
        name=org.name,
        description=org.description
    )
    db.add(db_org)
    db.commit()
    db.refresh(db_org)

    for service in org.services:
        db_service = Service(
            org_id=db_org.id,
            service_type=service.service_type,
            endpoint_url=service.endpoint_url
        )
        db.add(db_service)
    db.commit()
    return db_org

def get_organization(db: Session, org_id: str):
    return db.query(Organization).filter(Organization.org_id == org_id).first()
