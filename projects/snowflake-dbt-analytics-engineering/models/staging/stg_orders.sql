with source as (
    select *
    from {{ source('raw', 'orders') }}
),

renamed as (
    select
        cast(order_id as number) as order_id,
        cast(customer_id as number) as customer_id,
        cast(order_date as timestamp) as order_date,
        cast(updated_at as timestamp) as updated_at,
        cast(order_amount as number(18,2)) as order_amount,
        upper(trim(status)) as status
    from source
)

select * from renamed
