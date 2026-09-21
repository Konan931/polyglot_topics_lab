-- PostgreSQL foundation schema for Polyglot Topics Lab.

create table if not exists topics (
    id text primary key check (id like 'topic.%'),
    canonical_name text not null,
    entity_type text not null,
    difficulty smallint not null check (difficulty between 1 and 5),
    summary_short text not null,
    metadata_status text not null check (metadata_status in ('generated_seed', 'curated', 'reviewed'))
);

create table if not exists aliases (
    topic_id text not null references topics(id) on delete cascade,
    alias text not null,
    primary key (topic_id, alias)
);

create table if not exists categories (
    id text primary key,
    label text not null,
    description text not null
);

create table if not exists topic_categories (
    topic_id text not null references topics(id) on delete cascade,
    category_id text not null references categories(id) on delete cascade,
    is_primary boolean not null default false,
    weight real not null default 1.0 check (weight >= 0 and weight <= 1),
    primary key (topic_id, category_id)
);

create table if not exists relations (
    id text primary key check (id like 'relation.%'),
    source_id text not null references topics(id) on delete cascade,
    target_id text not null references topics(id) on delete cascade,
    relation_type text not null,
    weight real not null default 1.0 check (weight >= 0 and weight <= 1),
    metadata_status text not null check (metadata_status in ('generated_seed', 'curated', 'reviewed')),
    check (source_id <> target_id)
);

create index if not exists idx_topics_name on topics (canonical_name);
create index if not exists idx_topic_categories_category on topic_categories (category_id, topic_id);
create index if not exists idx_relations_source on relations (source_id, relation_type);
create index if not exists idx_relations_target on relations (target_id, relation_type);
