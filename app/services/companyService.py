from sqlalchemy.orm import Session
from models.company import Company
from schemas.company import CompanyView, CompanyModel
from services.exceptionService import ExceptionService
from uuid import UUID
class CompanyService:
    def __init__(self):
        self.company_model = Company
        self.exception_service = ExceptionService()

    def create_new_company( self, company_request: CompanyModel, db: Session) -> CompanyView | None:
        new_company = self.company_model(**company_request.model_dump())
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
        return new_company
    
    def get_detail(self, id: UUID, db: Session):
        company = db.query(self.company_model).filter(self.company_model == id).first()
        if not company:
            raise self.exception_service.NotFoundException(self.company_model)
        return company
    
    def get_all_company(self, db: Session):
        return db.query(self.company_model).all()
    
    def update_company(self, company_request: CompanyModel, id: UUID, db: Session) -> CompanyView:
        company = db.query(self.company_model).filter(self.company_model.company_id == id).first()
        if not company:
            raise self.exception_service.NotFoundException(self.company_model)
        
        company.name = company_request.name
        company.description = company_request.description
        company.mode = company_request.mode
        company.rating = company_request.rating

        db.add(company)
        db.flush()
        db.commit()
        return company


    def delete_company(self, uuid: UUID, db: Session) -> None:
        company = db.query(self.company_model).filter(self.company_model.company_id == uuid).first()
        if not company:
            raise self.exception_service.NotFoundException(self.company_model)
        db.delete(company)
        db.commit()
        return "Delete company successfully!"