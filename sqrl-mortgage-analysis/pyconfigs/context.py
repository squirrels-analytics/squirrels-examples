from typing import Any
from squirrels import ContextArgs, parameters as p


def main(ctx: dict[str, Any], sqrl: ContextArgs) -> None:
    if sqrl.param_exists("loan_amount"):
        loan_amount_param: p.TextParameter = sqrl.prms["loan_amount"]
        ctx["loan_amount"] = loan_amount_param.get_entered_text().apply_as_number(float)
    
    if sqrl.param_exists("mortgage_rate"):
        mortgage_rate_param: p.NumberParameter = sqrl.prms["mortgage_rate"]
        annual_rate = mortgage_rate_param.get_selected_value() / 100

        if sqrl.param_exists("compound_periods"):
            compound_periods_param: p.SingleSelectParameter = sqrl.prms["compound_periods"]
            num_compound_periods = int(compound_periods_param.get_selected_id())
        else:
            num_compound_periods = 2

        ctx["applied_monthly_rate"] = (1 + annual_rate / num_compound_periods) ** (num_compound_periods / 12) - 1

    ctx["total_num_months"] = 0
    if sqrl.param_exists("num_years"):
        num_years_param: p.NumberParameter = sqrl.prms["num_years"]
        ctx["total_num_months"] += 12 * int(num_years_param.get_selected_value())
    
    if sqrl.param_exists("num_months"):
        num_months_param: p.NumberParameter = sqrl.prms["num_months"]
        ctx["total_num_months"] += int(num_months_param.get_selected_value())
    
    if sqrl.param_exists("start_date"):
        start_date_param: p.DateParameter = sqrl.prms["start_date"]
        ctx["start_date"] = start_date_param.get_selected_date()

    if "loan_amount" in ctx and "applied_monthly_rate" in ctx and "total_num_months" in ctx:
        loan, rate, num_months = ctx["loan_amount"], ctx["applied_monthly_rate"], ctx["total_num_months"]
        ctx["monthly_payment"] = loan * rate / (1 - (1 + rate) ** -num_months)

    if sqrl.param_exists("mortgage_payment"):
        mortgage_payment_param: p.TextParameter = sqrl.prms["mortgage_payment"]
        ctx["mortgage_payment"] = mortgage_payment_param.get_entered_text().apply_as_number(float)
    
    if sqrl.param_exists("num_trials"):
        num_trials_param: p.NumberParameter = sqrl.prms["num_trials"]
        ctx["num_trials"] = int(num_trials_param.get_selected_value())
