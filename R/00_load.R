# Base-R loader for the generated TSV view.
script_path <- if (!is.null(sys.frame(1)$ofile)) sys.frame(1)$ofile else file.path("R", "00_load.R")
root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)

topics_path <- file.path(root, "data", "generated", "topics.tsv")
relations_path <- file.path(root, "data", "generated", "relations.tsv")

topics <- read.delim(topics_path, sep = "\t", quote = "", stringsAsFactors = FALSE, check.names = FALSE)
relations <- read.delim(relations_path, sep = "\t", quote = "", stringsAsFactors = FALSE, check.names = FALSE)
