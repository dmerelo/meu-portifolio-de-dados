{% snapshot orders_snapshot %}

{{
    config(
      target_schema='SNAPSHOTS',
      unique_key='order_id',
      strategy='timestamp',
      updated_at='updated_at'
    )
}}

select *
from {{ source('raw', 'orders') }}

{% endsnapshot %}
