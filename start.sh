#!/bin/sh

alembic upgrade head

fastapi dev --host 0.0.0.0 ./src/main.py