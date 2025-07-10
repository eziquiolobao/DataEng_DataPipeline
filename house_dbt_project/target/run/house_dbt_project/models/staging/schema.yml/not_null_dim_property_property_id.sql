select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select property_id
from HOUSEMARKET.MA_HOUSES_ma_houses.dim_property
where property_id is null



      
    ) dbt_internal_test