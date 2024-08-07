"""Company services"""
from uuid import UUID
from app.models.company import Company
from app.schemas.company import CompanyView, CompanyModel
from app.services.exceptionService import ExceptionService
from sqlalchemy.orm import Session

class CompanyService:
    """Company Service class"""
    def __init__(self):
        self.company_model = Company
        self.exception_service = ExceptionService()

    def create_new_company( self, company_request: CompanyModel, db: Session) -> CompanyView | None:
        """create new company"""
        new_company = self.company_model(
            name=company_request.name,
            description=company_request.description,
            mode=company_request.mode,
            rating=company_request.rating
        )
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
        return new_company

    def get_detail(self, company_id: UUID, db: Session):
        """get detail"""
        company = db.query(self.company_model).filter(self.company_model.company_id == company_id).first()
        if not company:
            raise self.exception_service.NotFoundException(self.company_model)
        return company

    def get_all_company(self, db: Session):
        """get all company"""
        return db.query(self.company_model).all()
    def update_company(self, company_request: CompanyModel, company_id: UUID, db: Session) -> CompanyView:
        """update company"""
        company = db.query(self.company_model).filter(self.company_model.company_id == company_id).first()
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
        """delete company"""
        company = db.query(self.company_model).filter(self.company_model.company_id == uuid).first()
        if not company:
            raise self.exception_service.NotFoundException(self.company_model)
        db.delete(company)
        db.commit()
        return "Delete company successfully!"
