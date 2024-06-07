from sqlalchemy import and_
from sqlalchemy.orm import Session
from models.users import User
from schemas.users import UserModel, UserView, UserUpdateInformation
from services.exceptionService import ExceptionService
from uuid import UUID
from typing import Optional
from sqlalchemy.sql.elements import BooleanClauseList
from services.auth_services import AuthService
class UserSerivce:
    def __init__(self):
        self.user_model = User
        self.exception_service = ExceptionService()
        self.auth_service = AuthService()
    
    def _filter_user(
        self,
        is_admin: Optional[str] = None,
        is_active: Optional[str] = None,
        company_id: Optional[str] = None,
    ) -> BooleanClauseList:
        domains = []

        if is_admin is not None:
            domains.append(self.user_model.is_admin == is_admin)

        if is_active is not None:
            domains.append(self.user_model.is_active == is_active)

        if company_id:
            domains.append(self.user_model.company_id.in_([company_id]))

        return and_(*domains)

    def create_new_user(self, user: UserModel, db: Session) -> UserView | None:
        hashed_password = self.auth_service.get_password_hash(user.password)
        new_user = self.user_model(
            email=user.email,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            is_active=user.is_active,
            is_admin=user.is_admin,
            company_id=user.company_id,
            hashed_password=hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
    def get_detail(self, id: UUID, db: Session):
        user = db.query(self.user_model).filter(self.user_model == id).first()
        if not user:
            raise self.exception_service.NotFoundException(self.user_model)
    def get_all_users(self, db: Session):
        return db.query(self.user_model).all()

    def update_user(self, user_request: UserUpdateInformation, id: UUID, db: Session) -> UserView:
        user = db.query(self.user_model).filter(self.user_model.id == id).first()
        if not user:
            raise self.exception_service.NotFoundException(self.user_model)
        
        for key, value in user_request.dict(exclude_unset=True).items():
            setattr(user, key, value)

        user.save(db)

        return user


    def delete_user(self, uuid: UUID, db: Session) -> None:
        user = db.query(self.user_model).filter(self.user_model.id == uuid).first()
        if not user:
            raise self.exception_service.NotFoundException(self.user_model)
        db.delete(user)
        db.commit()