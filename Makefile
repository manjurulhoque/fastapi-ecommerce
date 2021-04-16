.DEFAULT_GOAL := run

run:
	uvicorn app.main:app --reload --port 8700

migrate:
	alembic upgrade head

downgrade:
	alembic downgrade -1 // downgrade latest revision