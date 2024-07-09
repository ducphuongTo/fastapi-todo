"""Company routers"""
from uuid import UUID
from schemas.company import CompanyView, CompanyModel
from services.companyService import CompanyService
from database import get_db_context
from constants.routers import (
    ROUTE_COMPANY,
    ROUTE_CREATE,ROUTE_GET_BY_ID,
    ROUTE_UPDATE_BY_ID,
    ROUTE_DELETE_BY_ID
)
from starlette import status
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
router = APIRouter(prefix=ROUTE_COMPANY, tags=["Company"])
company_service = CompanyService()

@router.get("")
async def get_all_companys(db: Session=Depends(get_db_context)):
    """get all company"""
    return company_service.get_all_company(db)

@router.get(ROUTE_GET_BY_ID)
async def get_company_detail(company_id: UUID, db: Session=Depends(get_db_context)):
    """Get comapny detail"""
    try:
        company = company_service.get_detail(company_id, db)
        return company
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.post(ROUTE_CREATE, response_model=CompanyView, status_code=status.HTTP_201_CREATED)
async def create_new_companay(request: CompanyModel, db: Session=Depends(get_db_context)):
    """Company routers"""
    try:
        result = company_service.create_new_company(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.put(ROUTE_UPDATE_BY_ID, response_model=CompanyView)
async def update_company(
        request: CompanyModel,
        company_id: UUID, db:
        Session=Depends(get_db_context)
    ):
    """Update company"""
    result = company_service.update_company(request, company_id, db)
    return result

@router.delete(ROUTE_DELETE_BY_ID)
def delete_company(uuid: UUID, db: Session=Depends(get_db_context)) -> None:
    """Delete company"""
    company_service.delete_company(uuid, db)
