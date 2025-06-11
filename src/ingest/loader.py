import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

def load_data_to_postgres(df: pd.DataFrame, db_url: str, table_name: str = "gold_prices") -> None:
    """
    Guarda los datos en una tabla PostgreSQL usando SQLAlchemy.

    Args:
        df (pd.DataFrame): DataFrame ya validado y limpio.
        db_url (str): URL de conexión a la base de datos PostgreSQL.
        table_name (str): Nombre de la tabla destino (por defecto 'gold_prices').
    """
    try:
        # Creo el motor de conexión a la base de datos
        engine: Engine = create_engine(db_url)

        # Si el índice está nombrado, lo transformamos en columna
        if df.index.name is not None:
            df = df.reset_index()

        # Insertamos los datos en la tabla
        df.to_sql(table_name, engine, if_exists='append', index=False)

        print(f"{len(df)} filas insertadas correctamente en la tabla '{table_name}'.")

    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")
