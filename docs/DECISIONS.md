# Decision Log

## D-001 — One canonical model

**Decision:** Keep one normalized knowledge model and derive language-specific views from it.

**Reason:** Prevent divergent datasets across R, Julia, Python, SQL, Go, C, and the web layer.

## D-002 — Preserve explicit relations

**Decision:** Typed graph relations remain first-class data even after embeddings are introduced.

**Reason:** Semantic similarity does not explain why two concepts are related.

## D-003 — Julia is a scientific engine

**Decision:** Julia is reserved for meaningful scientific-computing, graph, numerical, and visualization work rather than simple format-reading demos.

## D-004 — Deployment comes after local integrity

**Decision:** Supabase and Vercel integration follow schema and dataset validation.

**Reason:** External infrastructure should not stabilize an immature data model.
