from squirrels import ConnectionsArgs
from sqlalchemy import Engine
import pickle


def main(connections: dict[str, Engine], sqrl: ConnectionsArgs) -> None:
    
    with open("assets/ice_cream_sales_model.pkl", 'rb') as f:
        connections["ice_cream_regr_model"] = pickle.load(f)
