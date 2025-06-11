import pandas as pd


def fetch_mql5_csv(filepath: str, symbol: str = "XAU/USD", timeframe: str = "M1")-> pd.DataFrame:
    """
    Carga y transforma un archivo csv exportado desde (MQL5)
    
    Arguments:
          filepath (str): Ruta del archivo .csv exportado por MT5.
        symbol (str): Nombre del instrumento (por defecto: 'XAU/USD').
        timeframe (str): Intervalo de tiempo (ej: 'M1', 'M5', 'tick').
    return:
        pd.DataFrame: Datos transformados con columnas estandarizadas.
    """

    try:
        # Cargamos el archivo .CSV
        df = pd.read_csv(filepath)

        # Verificamos que las columnas esperadas existan
        expected = ["time", "open", "high", "low", "close", "volume"]
        if not all(col in df.columns for col in expected):
            raise ValueError("Formato inesperado. Se requiere columnas: " + ", ".join(expected))

        # Es importante parsear el tiempo al formato datetime
        df["timestamp"] = pd.to_datetime(df["time"], format="%d/%m/%Y %H:%M:%S")

        # Reordenamos columnas y agregamos identificadores
        df = df[["timestamp", "open", "high", "low", "close", "volume"]]
        df["symbol"] = symbol
        df["timeframe"] = timeframe

        return df

    except Exception as e:
        print(f"Error en el procesado del archivo CSV: {e}")
        return pd.DataFrame()