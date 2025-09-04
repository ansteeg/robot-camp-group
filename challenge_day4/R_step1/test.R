# fix_people_json.R

# 1) Load jsonlite (install if needed)
if (!requireNamespace("jsonlite", quietly = TRUE)) {
  install.packages("jsonlite", repos = "https://cran.rstudio.com/")
}
library(jsonlite)

# 2) Resolve input/output paths
#    - If you pass a path as an argument, use it.
#    - Otherwise look for "data1.json" in the script's folder (or working dir when sourced).
args <- commandArgs(trailingOnly = TRUE)

args_all  <- commandArgs(trailingOnly = FALSE)
file_arg  <- sub("^--file=", "", grep("^--file=", args_all, value = TRUE))
scriptdir <- if (length(file_arg)) dirname(normalizePath(file_arg)) else getwd()

json_in  <- if (length(args) >= 1) args[1] else file.path(scriptdir, "data1.json")
json_out <- file.path(scriptdir, "data2.json")

if (!file.exists(json_in)) {
  stop(sprintf("Can't find JSON at: %s\nWorking dir: %s", json_in, getwd()))
}

# 3) Read JSON
json_data <- fromJSON(json_in, simplifyVector = TRUE)

# 4) Ensure 'people' is a data frame and keep original key names (with spaces)
people_df <- as.data.frame(json_data$people, stringsAsFactors = FALSE, check.names = FALSE)

# 5) Fill NAs in numeric columns with column means
num_cols <- vapply(people_df, is.numeric, logical(1))
for (nm in names(people_df)[num_cols]) {
  m <- mean(people_df[[nm]], na.rm = TRUE)
  if (!is.na(m)) {
    people_df[[nm]][is.na(people_df[[nm]])] <- m
  }
}

# 6) Put back and write out
json_data$people <- people_df
json_text <- toJSON(json_data, pretty = TRUE, auto_unbox = TRUE, na = "null")
writeLines(json_text, json_out)
cat("Wrote:", json_out, "\n")
