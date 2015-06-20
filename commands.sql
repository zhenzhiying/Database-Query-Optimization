explain select *
from basic;

#----------------------------------------------------------

explain select name
from basic;

#----------------------------------------------------------

explain select distinct name
from basic;

#----------------------------------------------------------

explain select *
from basic
where shop_id=10328540;

#----------------------------------------------------------

explain select *
from basic
where shop_id>10328540 and shop_id<10329940;

#----------------------------------------------------------

explain select *
from basic
where name='林师傅';

create index index_name on basic(name);

#----------------------------------------------------------

explain select name
from basic
where avg_price<50;

create index index_name_price on basic(avg_price,name);
