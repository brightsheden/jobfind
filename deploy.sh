#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running Alembic migrations..."
alembic upgrade head
echo "Alembic migrations complete."