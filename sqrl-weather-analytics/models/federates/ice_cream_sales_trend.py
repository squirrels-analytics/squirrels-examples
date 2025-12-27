from squirrels import ModelArgs
from sklearn.linear_model import LinearRegression
import polars as pl, numpy as np


def main(sqrl: ModelArgs) -> pl.LazyFrame:
    """
    Create federated models by joining/processing dependent database views and/or other federated models to
    form and return the result as a new pandas DataFrame.
    """
    df_weather: pl.LazyFrame = sqrl.ref("dbv_weather_by_date")
    df_ice_cream: pl.LazyFrame = sqrl.ref("dbv_ice_cream_sales")

    ## Join dataframes
    df_joined = df_weather.join(df_ice_cream, on="date")

    ## Get ML model
    model: LinearRegression = sqrl.connections["ice_cream_regr_model"]
    
    ## Make prediction
    df_joined = df_joined.with_columns(temperature_c=pl.col("temperature_max"))
    
    # Collect the data from the lazyframe
    temperature_values = df_joined.select("temperature_c").collect().to_series().to_numpy().reshape(-1, 1)
    prediction = model.predict(temperature_values)
    
    df_joined = df_joined.with_columns(expected_profit=pl.lit(np.round(prediction, 2)))

    ## Select columns and convert back to pandas
    df = df_joined.select(["date", "ice_cream_profits", "temperature_c", "expected_profit"])
    return df