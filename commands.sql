explain select *
from basic
where name='林师傅';

create index index_name on basic(name);

#----------------------------------------------------------

explain select phone
from basic
where name='巫山烤全鱼' and avg_price<50;

create index index_name on basic(name);