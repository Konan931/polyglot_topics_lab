-- Level 03: count membership across categories.
select c.label, count(*) as topic_count
from categories as c
join topic_categories as tc on tc.category_id = c.id
group by c.id, c.label
order by topic_count desc, c.label;
