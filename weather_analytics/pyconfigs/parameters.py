import squirrels as sr


def main(sqrl: sr.ParametersArgs) -> None:

    # Group by
    group_by_options = [
        sr.SelectParameterOption("0", "Year", dim_col="year"),
        sr.SelectParameterOption("1", "Quarter", dim_col="quarter"),
        sr.SelectParameterOption("2", "Month", dim_col="month_name", order_by_col="month_order"),
        sr.SelectParameterOption("3", "Day of Year", dim_col="day_of_year"),
        sr.SelectParameterOption("4", "Condition", dim_col="condition")
    ]
    sr.SingleSelectParameter.CreateSimple("group_by", "Group By", group_by_options)

    # Trend type
    trend_type_options = [
        sr.SelectParameterOption("0", "Weather Over Years", dim_col="start_of_year", alias="year"),
        sr.SelectParameterOption("1", "Weather Over Quarters", dim_col="start_of_quarter", alias="quarter_of"),
        sr.SelectParameterOption("2", "Weather Over Months", dim_col="start_of_month", alias="month_of"),
        sr.SelectParameterOption("3", "Weather Over Weeks", dim_col="start_of_week", alias="week_of")
    ]
    sr.SingleSelectParameter.CreateSimple("trend_type", "Trend Type", trend_type_options)

    # Time type
    time_type_options = sr.SingleSelectDataSource('time_type', 'index', 'value', custom_cols={'column': 'column'})
    sr.SingleSelectParameter.CreateFromSource("time_type", "Time Period Type", time_type_options)

    # Time periods
    time_period_options = sr.MultiSelectDataSource("time_lookup", "index", "start_of_time", parent_id_col="time_type_id")
    sr.MultiSelectParameter.CreateFromSource("time_periods", "Time Period Options", time_period_options, parent_name="time_type")
