sleep 5 # wait for database startup (this logic is valid, while running app locally through docker-compose
cd app
alembic upgrade heads
uvicorn main:app --host 0.0.0.0 --port 8000
