{% macro cents_to_currency(column_name) %}
    ({{ column_name }} / 100.0)
{% endmacro %}
