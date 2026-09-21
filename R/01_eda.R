# Exploratory summaries over the generated topic view.
source(file.path("R", "00_load.R"))

cat("Topics:", nrow(topics), "\n")
cat("Relations:", nrow(relations), "\n\n")

category_tokens <- unlist(strsplit(topics$categories, "\\|"))
category_counts <- sort(table(category_tokens), decreasing = TRUE)
print(category_counts)

cat("\nDifficulty distribution:\n")
print(table(topics$difficulty))
