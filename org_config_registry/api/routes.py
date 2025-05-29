from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.pydantic_models import OrgCreate, OrgResponse
from core.db import SessionLocal
from crud.operations import create_organization, get_organization
from fastapi import APIRouter, Depends, HTTPException
from shared.auth import verify_token, create_org_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/orgs", response_model=OrgResponse)
def register_org(org: OrgCreate, token_org: str = Depends(verify_token), db: Session = Depends(get_db)):
    if token_org != org.org_id:
        raise HTTPException(status_code=403, detail="Token does not match org_id")
    existing = get_organization(db, org.org_id)
    if existing:
        raise HTTPException(status_code=409, detail="Organization already exists.")
    return create_organization(db, org)

@router.get("/orgs/{org_id}", response_model=OrgResponse)
def fetch_org(org_id: str, token_org: str = Depends(verify_token), db: Session = Depends(get_db)):
    if token_org != org_id:
        raise HTTPException(status_code=403, detail="Access denied to this org")
    org = get_organization(db, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Org not found.")
    return org

@router.get("/auth/token/{org_id}")
def generate_token(org_id: str):
    return {"token": create_org_token(org_id)}
