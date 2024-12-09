from typing import Iterable
from squirrels import ModelArgs, ModelDepsArgs
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd


def dependencies(sqrl: ModelDepsArgs) -> Iterable:
    return ["seed_snp500"]


def main(sqrl: ModelArgs) -> pd.DataFrame:
    (df_snp,) = [sqrl.ref(name) for name in dependencies(sqrl)]

    start_date = sqrl.get_placeholder_value("start_date")
    total_num_months = sqrl.ctx["total_num_months"]
    monthly_payment = sqrl.ctx["monthly_payment"]

    curr_month = datetime.strptime(start_date, "%Y-%m-%d")
    loan_amount = sqrl.ctx["loan_amount"]

    stock_returns = df_snp["relative_change"].sample(total_num_months, replace=True)

    prev_row = {
        "month_number": 0,
        "current_month": curr_month.strftime("%Y-%m-%d"),
        "stock_return": None,
        "deposit_if_renew_mortgage": loan_amount,
        "value_if_renew_mortgage": loan_amount,
        "deposit_if_pay_down_house": 0,
        "value_if_pay_down_house": 0
    }

    rows = [prev_row]
    for idx in range(total_num_months):
        curr_month = curr_month + relativedelta(months=1)
        stock_return = stock_returns.values[idx]
        row = {
            "month_number": idx + 1,
            "current_month": curr_month.strftime("%Y-%m-%d"),
            "stock_return": stock_return,
            "deposit_if_renew_mortgage": 0,
            "value_if_renew_mortgage": prev_row["value_if_renew_mortgage"] * (1 + stock_return),
            "deposit_if_pay_down_house": monthly_payment,
            "value_if_pay_down_house": prev_row["value_if_pay_down_house"] * (1 + stock_return) + monthly_payment
        }
        rows.append(row)
        prev_row = row

    df = pd.DataFrame(rows)

    dollars_columns = ["deposit_if_renew_mortgage", "value_if_renew_mortgage", "deposit_if_pay_down_house", "value_if_pay_down_house"]
    for col in dollars_columns:
        df[col] = df[col].round(2)

    return df
