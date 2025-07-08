# Data Engineering Pipeline for Harvard, MA Home Sales

This project demonstrates an end-to-end data engineering pipeline using **Airflow**, **dbt**, and **PostgreSQL** to analyze home sales data from Redfin.

## Components
- **Airflow** orchestrates the ingestion and transformation jobs.
- **PostgreSQL** stores the raw and transformed data.
- **dbt** models the data into facts, dimensions, and marts.
- **Docker Compose** provides a simple local setup.

## Quickstart
1. Ensure Docker and Docker Compose are installed.
2. Place your Redfin CSV at `data/redfin_harvard_ma.csv` or set `REDFIN_CSV_PATH`.
3. Run `docker-compose up` to start all services.
4. Access Airflow at `http://localhost:8080` (default credentials: `airflow/airflow`).
5. Trigger the `redfin_data_pipeline` DAG to load and transform the data.
6. Customize PostgreSQL credentials via environment variables in `docker-compose.yml` if needed.

## dbt
The dbt project lives in `redfin_dbt_project`. It includes models:
- `stg_redfin_sales` – staging view for raw data.
- `fact_sales` – cleaned fact table.
- `dim_property` – dimension of unique properties.
- `mart_monthly_trends` – aggregates for price trends.

To run dbt manually inside the container:
```bash
docker-compose run dbt dbt run
```

## Testing
Run dbt tests:
```bash
docker-compose run dbt dbt test
```

## Airflow DAG
The DAG defined in `airflow/dags/redfin_pipeline_dag.py` performs:
1. Load the CSV into PostgreSQL.
2. Execute `dbt run`.
3. Print completion message.

## PostgreSQL Setup
The table DDL can be found in `sql/create_staging_table.sql` and is executed automatically when the database container starts.

## Documentation
Generate dbt docs:
```bash
docker-compose run dbt dbt docs generate
```
Then serve docs:
```bash
docker-compose run --service-ports dbt dbt docs serve
```

