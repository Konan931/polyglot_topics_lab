-- Level 04: inspect explicit outgoing relationships.
select
    source.canonical_name as source_topic,
    r.relation_type,
    target.canonical_name as target_topic
from relations as r
join topics as source on source.id = r.source_id
join topics as target on target.id = r.target_id
where source.canonical_name = 'Bauhaus'
order by r.relation_type, target.canonical_name;
