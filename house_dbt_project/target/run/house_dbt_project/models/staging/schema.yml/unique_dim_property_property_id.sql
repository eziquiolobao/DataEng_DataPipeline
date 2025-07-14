select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    property_id as unique_field,
    count(*) as n_records

from HOUSEMARKET.MA_HOUSES_ma_houses.dim_property
where property_id is not null
group by property_id
having count(*) > 1



      
    ) dbt_internal_test