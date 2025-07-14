with base as (
    select * from {{ ref('fact_sales') }}
)
, monthly as (
    select
        date_trunc('month', to_date(sold_date)) as month,
        sum(price) as total_sales,
        avg(price / nullif(square_feet,0)) as price_per_sqft
    from base
    group by 1
)
select * from monthly
