SELECT ri.REST_ID, ri.REST_NAME, ri.FOOD_TYPE, ri.FAVORITES, ri.ADDRESS, ROUND(avg(rv.REVIEW_SCORE),2) as SCORE
from REST_INFO ri
join REST_REVIEW rv on ri.REST_ID = rv.REST_ID
where ri.ADDRESS LIKE '서울%'
group by
    ri.REST_ID, 
    ri.REST_NAME, 
    ri.FOOD_TYPE, 
    ri.FAVORITES, 
    ri.ADDRESS
order by SCORE desc, ri.FAVORITES desc;