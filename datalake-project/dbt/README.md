# datalake-project/dbt/README.md

# DBT Project Documentation

This README provides an overview of the DBT (Data Build Tool) project within the datalake-project. It includes setup instructions, usage guidelines, and information about the project's structure.

## Project Structure

- **models/**: Contains SQL models that define transformations to be applied to the data.
- **seeds/**: Directory for seed data files that can be loaded into the database.
- **snapshots/**: Directory for snapshot files that capture the state of data at a specific point in time.
- **dbt_project.yml**: Configuration file for the DBT project, specifying project settings and configurations.

## Setup Instructions

1. Ensure you have DBT installed. You can install it using pip:

   ```
   pip install dbt
   ```

2. Navigate to the DBT directory:

   ```
   cd dbt
   ```

3. Configure your `dbt_project.yml` file according to your database settings.

4. To run the models, use the following command:

   ```
   dbt run
   ```

5. To test your models, use:

   ```
   dbt test
   ```

## Usage Guidelines

- Place your SQL transformation models in the `models/` directory.
- Use the `seeds/` directory for any CSV files that you want to load into your database.
- Utilize the `snapshots/` directory to create snapshots of your data at specific intervals.

For more detailed information on DBT, refer to the official [DBT documentation](https://docs.getdbt.com/).