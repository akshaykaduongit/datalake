def fetch_data_from_db(connection_string, query):
    import pandas as pd
    import sqlalchemy

    # Create a database connection
    engine = sqlalchemy.create_engine(connection_string)
    
    # Fetch data using the provided query
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    
    return result

def fetch_all_tables(connection_string):
    import pandas as pd
    import sqlalchemy

    # Create a database connection
    engine = sqlalchemy.create_engine(connection_string)
    
    # Fetch all table names
    with engine.connect() as connection:
        tables = connection.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'").fetchall()
    
    return [table[0] for table in tables]