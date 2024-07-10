{%- import 'macros/transaction_features.j2' as tf -%}

SELECT DISTINCT {{ tf.full_name() }} as first_last_name, 
    cc_num, street, zip, job
FROM transactions
WHERE TRUE 
{% if is_placeholder("name_pattern") -%} AND {{ tf.full_name() }} LIKE :name_pattern {%- endif %}
