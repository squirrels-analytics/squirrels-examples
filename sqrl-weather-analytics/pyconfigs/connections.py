from squirrels import ConnectionsArgs, ConnectionProperties
from sqlalchemy import text
from sklearn.linear_model import LinearRegression
import json
import numpy as np


def main(connections: dict[str, ConnectionProperties], sqrl: ConnectionsArgs) -> None:

    # Test connection
    with connections["duckdb"].engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    
    with open("assets/ice_cream_sales_model.json", 'r') as f:
        model_data = json.load(f)
        params = model_data["parameters"]
    
    model = LinearRegression()
    model.coef_ = np.array([params["a"]])
    model.intercept_ = params["b"]
    
    connections["ice_cream_regr_model"] = model
