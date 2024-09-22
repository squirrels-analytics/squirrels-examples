SELECT DISTINCT {{ full_name() }} as first_last_name, 
    cc_num, street, zip, job
FROM transactions
WHERE TRUE 
{% if is_placeholder("name_pattern") -%} AND {{ full_name() }} LIKE :name_pattern {%- endif %}
