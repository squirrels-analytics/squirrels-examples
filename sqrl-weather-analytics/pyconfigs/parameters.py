from squirrels import ParametersArgs, parameters as p, parameter_options as po


def main(sqrl: ParametersArgs) -> None:

    ## Group by
    group_by_options = [
        po.SelectParameterOption("0", "Year", dim_col="year"),
        po.SelectParameterOption("1", "Quarter", dim_col="quarter"),
        po.SelectParameterOption("2", "Month", dim_col="month_name", order_by_col="month_order"),
        po.SelectParameterOption("3", "Day of Year", dim_col="day_of_year"),
        po.SelectParameterOption("4", "Condition", dim_col="condition")
    ]
    p.SingleSelectParameter.CreateSimple("group_by_dim", "Group By", group_by_options)

    ## Trend type
    trend_type_options = [
        po.SelectParameterOption("0", "Weather Over Years", dim_col="start_of_year", period_type="year_of"),
        po.SelectParameterOption("1", "Weather Over Quarters", dim_col="start_of_quarter", period_type="quarter_of"),
        po.SelectParameterOption("2", "Weather Over Months", dim_col="start_of_month", period_type="month_of"),
        po.SelectParameterOption("3", "Weather Over Weeks", dim_col="start_of_week", period_type="week_of")
    ]
    p.SingleSelectParameter.CreateSimple("trend_type", "Trend Type", trend_type_options)

    ## Date filter
    p.DateRangeParameter.CreateSimple("date_filter", "Date Range", default_start_date="2012-01-01", default_end_date="2015-12-31")
