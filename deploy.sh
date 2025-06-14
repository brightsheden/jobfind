#!/bin/bash

echo "Running Alembic migrations..."
alembic upgrade head
echo "Alembic migrations complete."