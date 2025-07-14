#!/bin/bash

# Wait for the DB to be up
sleep 10

# Initialize the DB (only if needed)
airflow db upgrade

# Create user only if not exists
airflow users create \
  --username "${AIRFLOW_USER}" \
  --password "${AIRFLOW_PASSWORD}" \
  --firstname Air \
  --lastname Flow \
  --role Admin \
  --email eziquio.souza@yahoo.com || true

# Start services
airflow scheduler & 
exec airflow webserver