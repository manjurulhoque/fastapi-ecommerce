.DEFAULT_GOAL := run

run:
	uvicorn app.main:app --reload

migrate:
	alembic upgrade head

downgrade:
	alembic downgrade -1 // downgrade latest revision