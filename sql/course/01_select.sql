-- Level 01: inspect the canonical topic table.
select id, canonical_name, difficulty
from topics
order by canonical_name;
