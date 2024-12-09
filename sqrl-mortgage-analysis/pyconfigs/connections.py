from squirrels import ConnectionsArgs
from sqlalchemy import Engine
from scipy import stats
import pandas as pd


def main(connections: dict[str, Engine], sqrl: ConnectionsArgs) -> None:
    df = pd.read_csv("seeds/seed_snp500.csv")
    mu, sigma = stats.norm.fit(df["relative_change"])
    connections["norm_dist_params"] = (mu, sigma)
