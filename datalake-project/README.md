# datalake-project

This project is designed to facilitate data fetching, transformation, and loading using DBT and Airflow. It includes a structured approach to manage data from various sources, ensuring a clean and efficient workflow.

## Project Structure

- **airflow/**: Contains the Airflow DAGs and requirements for orchestrating data fetching tasks.
  - **dags/**: Directory for Airflow Directed Acyclic Graphs (DAGs).
  - **requirements.txt**: Lists the dependencies required for the Airflow project.

- **dbt/**: Contains the DBT models, seeds, snapshots, and configuration.
  - **models/**: Directory for DBT transformation models.
  - **seeds/**: Directory for seed data files.
  - **snapshots/**: Directory for snapshot files.
  - **dbt_project.yml**: Configuration file for the DBT project.
  - **README.md**: Documentation specific to the DBT project.

- **src/**: Contains Python code for fetching data from various sources.
  - **data_fetchers/**: Directory for data fetching modules.
    - **fetch_from_api.py**: Functions to fetch data from APIs.
    - **fetch_from_db.py**: Functions to fetch data from databases.
    - **fetch_from_file.py**: Functions to fetch data from local files.
  - **__init__.py**: Marks the src directory as a Python package.

- **requirements.txt**: Lists the dependencies required for the overall project.

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies:
   - For Airflow: `pip install -r airflow/requirements.txt`
   - For the overall project: `pip install -r requirements.txt`
4. Configure Airflow and DBT as per your environment requirements.
5. Run the Airflow scheduler and web server to start orchestrating data fetching tasks.

## Usage Guidelines

- Use the `src/data_fetchers` modules to implement data fetching logic from various sources.
- Define your data transformation models in the `dbt/models` directory.
- Schedule and manage your data fetching tasks using the Airflow DAGs defined in the `airflow/dags` directory.

This project aims to provide a robust framework for managing data workflows efficiently.