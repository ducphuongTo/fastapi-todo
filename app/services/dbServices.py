from typing import Optional


from fastapi import Depends


from database import LocalSession



class DatabaseService:
    def __init__(self, model: Optional[any] = None):
        self.local_session = LocalSession()
        self.model = model

    def _get_db_context(self):
        db = self.local_session

        try:
            yield db
        finally:
            db.close()

    def get_session(self):
        return Depends(self._get_db_context)

    