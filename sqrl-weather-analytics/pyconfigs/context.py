from typing import Any
from squirrels import ContextArgs, parameters as p


def main(ctx: dict[str, Any], sqrl: ContextArgs) -> None:
    if sqrl.param_exists("group_by_dim"):
        group_by_param: p.SingleSelectParameter = sqrl.prms["group_by_dim"]
        ctx["dim_col"] = group_by_param.get_selected("dim_col")
        ctx["order_col"] = group_by_param.get_selected("order_by_col", default_field="dim_col")
    
    if sqrl.param_exists("trend_type"):
        trend_type_param: p.SingleSelectParameter = sqrl.prms["trend_type"]
        ctx["dim_col"] = trend_type_param.get_selected("dim_col")
        ctx["period_type"] = trend_type_param.get_selected("period_type")
    
    if sqrl.param_exists("date_filter"):
        date_filter_param: p.DateRangeParameter = sqrl.prms["date_filter"]
        sqrl.set_placeholder("start_date", date_filter_param.get_selected_start_date())
        sqrl.set_placeholder("end_date", date_filter_param.get_selected_end_date())
    