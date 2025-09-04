# Check if jsonlite is installed; if not, install it
if (!requireNamespace("jsonlite", quietly = TRUE)) {
  install.packages("jsonlite", repos = "https://cran.rstudio.com/")
}

# Load the required library
library(jsonlite)

# Read the JSON file into an R object
json_data <- fromJSON("data1.json")

# Convert the 'people' element to a data frame (if not already)
people_df <- as.data.frame(json_data$people)

# Replace NAs with column means (only for numeric columns)
for (col_name in names(people_df)) {
  if (is.numeric(people_df[[col_name]])) {
    col_mean <- mean(people_df[[col_name]], na.rm = TRUE)
    if (!is.nan(col_mean)) { # avoid replacing with NaN if entire column is NA
      people_df[[col_name]][is.na(people_df[[col_name]])] <- col_mean
    }
  }
}

# Put the modified data frame back into the JSON structure
json_data$people <- people_df

# Convert the updated object back to JSON format (pretty-printed)
json_text <- toJSON(json_data, pretty = TRUE)

# Save JSON to a new file
writeLines(json_text, "data2.json")
