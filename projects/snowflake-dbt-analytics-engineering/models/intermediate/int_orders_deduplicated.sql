with ranked as (
    select
        *,
        row_number() over (
            partition by order_id
            order by updated_at desc
        ) as rn
    from {{ ref('stg_orders') }}
)

select
    order_id,
    customer_id,
    order_date,
    updated_at,
    order_amount,
    status
from ranked
where rn = 1
