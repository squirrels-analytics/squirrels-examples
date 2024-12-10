from squirrels import ModelArgs
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd


def main(sqrl: ModelArgs) -> pd.DataFrame:
    start_date = sqrl.get_placeholder_value("start_date")
    current_month = datetime.strptime(start_date, "%Y-%m-%d")
    principal_remaining = sqrl.ctx["loan_amount"]

    rows = []
    for idx in range(sqrl.ctx["total_num_months"]):
        interest_payment = principal_remaining * sqrl.ctx["applied_monthly_rate"]
        principal_payment = sqrl.ctx["monthly_payment"] - interest_payment
        rows.append(
            {
                "month_number": idx + 1,
                "current_month": current_month.strftime("%Y-%m-%d"),
                "principal_start": principal_remaining,
                "payment": sqrl.ctx["monthly_payment"],
                "interest": interest_payment,
                "principal_payment": principal_payment
            }
        )
        current_month = current_month + relativedelta(months=1)
        principal_remaining = principal_remaining -  principal_payment

    df = pd.DataFrame(rows)
    return df.round(2)
