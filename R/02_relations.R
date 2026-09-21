# Relation-degree analysis without external packages.
source(file.path("R", "00_load.R"))

out_degree <- sort(table(relations$source_id), decreasing = TRUE)
in_degree <- sort(table(relations$target_id), decreasing = TRUE)

cat("Highest outgoing relation counts:\n")
print(head(out_degree, 10))
cat("\nHighest incoming relation counts:\n")
print(head(in_degree, 10))
