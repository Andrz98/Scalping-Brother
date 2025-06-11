import pandas as pd

def validate_gold_data(df: pd.DataFrame) -> bool:
    """
    Verifica que el DataFrame contenga las columnas necesarias y no contenga valores nulos.

    Args:
        df (pd.DataFrame): DataFrame a validar.

    Returns:
        bool: True si pasa todas las validaciones, False si falla.
    """
    required_columns = ["timestamp", "open", "high", "low", "close", "volume", "symbol", "timeframe"]

    # Verificamos que todas las columnas requeridas estén presentes
    for col in required_columns:
        if col not in df.columns:
            print(f"Falta columna requerida: {col}")
            return False

    # Verificamos que no haya valores nulos en columnas críticas
    if df[required_columns].isnull().any().any():
        print("Hay valores nulos en columnas críticas.")
        return False

    # Verificamos que la columna 'timestamp' sea tipo datetime
    if not pd.api.types.is_datetime64_any_dtype(df["timestamp"]):
        print("La columna 'timestamp' no es de tipo datetime.")
        return False

    return True
