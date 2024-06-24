from typing import Any
import squirrels as sr


def main(ctx: dict[str, Any], sqrl: sr.ContextArgs) -> None:

    if sqrl.prms_contain("group_by"):
        group_by_param: sr.SingleSelectParameter = sqrl.prms["group_by"]
        group_by_cols_list = group_by_param.get_selected("columns")
        order_by_cols_list = group_by_param.get_selected("aliases", default_field="columns")
        
        group_by_cols_list_select = []
        for column, alias in zip(group_by_cols_list, order_by_cols_list):
            if column != alias:
                group_by_cols_list_select.append(column + " as " + alias)
            else:
                group_by_cols_list_select.append(column)
                
        ctx["group_by_cols"] = ",".join(group_by_cols_list)
        ctx["group_by_cols_select"] = ",".join(group_by_cols_list_select)
        ctx["order_by_cols"] = ",".join(order_by_cols_list)

        join_cols_list = ["a." + item + " = b." + item for item in order_by_cols_list]
        ctx["join_cols"]  = " AND ".join(join_cols_list)

    if sqrl.prms_contain("gender"):
        category_param: sr.MultiSelectParameter = sqrl.prms["gender"]
        ctx["has_gender"] = category_param.has_non_empty_selection()
        ctx["gender"] = category_param.get_selected_labels_quoted_joined()

    if sqrl.prms_contain("percent_toggle"):
        percent_toggle_param: sr.SingleSelectParameter = sqrl.prms["percent_toggle"]
        ctx["percent_toggle"] = percent_toggle_param.get_selected_label()

    if sqrl.prms_contain("start_date"):
        start_date_param: sr.DateParameter = sqrl.prms["start_date"]
        sqrl.set_placeholder("start_date", start_date_param.get_selected_date())
    
    if sqrl.prms_contain("end_date"):
        end_date_param: sr.DateParameter = sqrl.prms["end_date"]
        sqrl.set_placeholder("end_date", end_date_param.get_selected_date())

    if sqrl.prms_contain("min_date_source"):
        min_date_param: sr.DateParameter = sqrl.prms["min_date_source"]
        sqrl.set_placeholder("start_date", min_date_param.get_selected_date())
    
    if sqrl.prms_contain("max_date_source"):
        max_date_param: sr.DateParameter = sqrl.prms["max_date_source"]
        sqrl.set_placeholder("end_date", max_date_param.get_selected_date())
    
    if sqrl.prms_contain("date_range"):
        range_filter: sr.DateRangeParameter = sqrl.prms["date_range"]
        sqrl.set_placeholder("end_date", range_filter.get_selected_end_date())
        sqrl.set_placeholder("start_date", range_filter.get_selected_start_date())
    
    if sqrl.prms_contain("job_category"):
        category_param: sr.MultiSelectParameter = sqrl.prms["job_category"]
        ctx["has_job_category"] = category_param.has_non_empty_selection()
        ctx["job_category"] = category_param.get_selected_labels_quoted_joined()
    
    if sqrl.prms_contain("job_subcategory"):
        subcategory_param: sr.MultiSelectParameter = sqrl.prms["job_subcategory"]
        ctx["has_job_subcategory"] = subcategory_param.has_non_empty_selection()
        ctx["job_subcategory"] = subcategory_param.get_selected_labels_quoted_joined()
    
    if sqrl.prms_contain("min_filter"):
        min_amount_filter: sr.NumberParameter = sqrl.prms["min_filter"]
        ctx["min_amount"] = min_amount_filter.get_selected_value()
    
    if sqrl.prms_contain("max_filter"):
        max_amount_filter: sr.NumberParameter = sqrl.prms["max_filter"]
        ctx["max_amount"] = max_amount_filter.get_selected_value()
    
    if sqrl.prms_contain("between_filter"):
        between_filter: sr.NumberRangeParameter = sqrl.prms["between_filter"]
        ctx["min_amount"] = between_filter.get_selected_lower_value()
        ctx["max_amount"] = between_filter.get_selected_upper_value()
    
    if sqrl.prms_contain("between_filter2"):
        between_filter: sr.NumberRangeParameter = sqrl.prms["between_filter2"]
        ctx["min_amount"] = between_filter.get_selected_lower_value()
        ctx["max_amount"] = between_filter.get_selected_upper_value()

    if sqrl.prms_contain("between_dob"):
        between_dob_filter: sr.DateRangeParameter = sqrl.prms["between_dob"]
        ctx["dob_end_date"] = between_dob_filter.get_selected_end_date_quoted()
        ctx["dob_start_date"] = between_dob_filter.get_selected_start_date_quoted()
    
    if sqrl.prms_contain("is_online"):
        is_online_filter: sr.SingleSelectParameter = sqrl.prms["is_online"]
        ctx["is_online"] = is_online_filter.get_selected_label()
    
    if sqrl.prms_contain("transaction_category"):
        transaction_category_filter: sr.MultiSelectParameter = sqrl.prms["transaction_category"]
        ctx["transaction_category"] = transaction_category_filter.get_selected_ids_quoted_joined()
    
    if sqrl.prms_contain("name_filter"):
        name_param: sr.TextParameter = sqrl.prms["name_filter"]
        name_pattern = name_param.get_entered_text().apply_percent_wrap()
        sqrl.set_placeholder("name_pattern", name_pattern)

    ctx["show_confidential"] = sqrl.traits.get("show_confidential", False)
    