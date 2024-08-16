from squirrels import ConnectionsArgs
from sqlalchemy import Engine, text
import pickle


def main(connections: dict[str, Engine], sqrl: ConnectionsArgs) -> None:

    # Test connection
    with connections["duckdb"].connect() as conn:
        conn.execute(text("SELECT 1"))
    
    with open("assets/ice_cream_sales_model.pkl", 'rb') as f:
        connections["ice_cream_regr_model"] = pickle.load(f)
