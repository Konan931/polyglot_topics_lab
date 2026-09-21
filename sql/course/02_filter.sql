-- Level 02: filter more advanced seed topics.
select canonical_name, entity_type, difficulty
from topics
where difficulty >= 4
order by difficulty desc, canonical_name;
