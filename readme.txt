1. Run postgres and pgadmin with docker : docker compose up --build
2. Go to /app folder and run uvicorn main:app --reload
3. Now connect to fastapi app at: localhost:8000
4. Pgadmin4 at localhost:8080
5. Connect to Pgadmin4 with email and password given in .env
6. Create connect with db_username and password given in .even
7. At /app, run migration with : alembic upgrade head