{%- set desc_pattern = prms["description_filter"].get_entered_text().apply_percent_wrap() -%}
{{- set_placeholder("desc_pattern", desc_pattern) -}}