{%- import 'macros/transaction_features.j2' as tf -%}

SELECT DISTINCT {{ tf.full_name() }} as first_last_name, 
    cc_num, street, zip, job
FROM transactions
