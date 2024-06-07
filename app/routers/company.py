from fastapi import APIRouter, Depends, HTTPException
from constants.routers import ROUTE_COMPANY, ROUTE_CREATE, ROUTE_GET_BY_ID, ROUTE_UPDATE_BY_ID, ROUTE_DELETE_BY_ID
from services.dbServices import DatabaseService
from sqlalchemy.orm import Session
from schemas.company import CompanyView, CompanyModel
from starlette import status
from services.companyService import CompanyService
from uuid import UUID
from database import get_db_context

router = APIRouter(prefix=ROUTE_COMPANY, tags=["Company"])
dbService = DatabaseService()
company_service = CompanyService()

@router.get("")
async def get_all_companys(db: Session=Depends(get_db_context)):
    return company_service.get_all_company(db)

@router.get(ROUTE_GET_BY_ID)
async def get_company_detail(company_id: UUID, db: Session=Depends(get_db_context)):
    try:
        company = company_service.get_detail(company_id, db)
        return company
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(ROUTE_CREATE, response_model=CompanyView, status_code=status.HTTP_201_CREATED)
async def create_new_companay(request: CompanyModel, db: Session=Depends(get_db_context)):
    try:
        result = company_service.create_new_company(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put(ROUTE_UPDATE_BY_ID, response_model=CompanyView)
async def update_company(request: CompanyModel, company_id: UUID, db: Session=Depends(get_db_context)):
    result = company_service.update_company(request, company_id, db)
    return result

@router.delete(ROUTE_DELETE_BY_ID)
def delete_company(uuid: UUID, db: Session=Depends(get_db_context)) -> None:
    company_service.delete_company(uuid, db)
