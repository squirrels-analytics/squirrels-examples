from typing import Any
import squirrels as sr


def main(ctx: dict[str, Any], sqrl: sr.ContextArgs) -> None:
    """
    Define context variables AFTER parameter selections are made by adding entries to the dictionary "ctx". 
    These context variables can then be used in the models.

    Note that the code here is used by all datasets, regardless of the parameters they use. You can use 
    sqrl.prms and sqrl.args to determine the conditions to execute certain blocks of code.
    """

    if "group_by" in sqrl.prms:
        group_by_param: sr.SingleSelectParameter = sqrl.prms["group_by"]
        ctx["dim_col"] = group_by_param.get_selected("dim_col")
        ctx["order_col"] = group_by_param.get_selected("order_by_col", default_field="dim_col")
    
    if "trend_type" in sqrl.prms:
        trend_type_param: sr.SingleSelectParameter = sqrl.prms["trend_type"]
        ctx["dim_col"] = trend_type_param.get_selected("dim_col")
        ctx["alias"] = trend_type_param.get_selected("alias")
    
    if "time_type" in sqrl.prms:
        time_type_param: sr.SingleSelectParameter = sqrl.prms["time_type"]
        ctx["filter_by_col"] = time_type_param.get_selected("column")
    
    if "time_periods" in sqrl.prms:
        time_periods_param: sr.MultiSelectParameter = sqrl.prms["time_periods"]
        ctx["has_time_periods"] = time_periods_param.has_non_empty_selection()
        ctx["selected_time_periods"] = time_periods_param.get_selected_labels_quoted_joined()
    