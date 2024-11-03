In this task, you’ll create a pivot table to explore how the popularity of different genres changes over time, based on user engagement. Specifically, you’ll look at the number of users per genre by year.

## Instructions

1. **Load and Prepare the Dataset**
   - Load the dataset from the provided path.
   - Fill any missing values in the `user_count` column with `0` (assuming missing values represent zero engagement).
   
2. **Create and Display a Pivot Table**
   - Create a pivot table with:
     - `genre` as the rows.
     - `year_of_release` as the columns.
     - `user_count` as the values, using `sum` as the aggregation function.
   - This pivot table should reflect the total `user_count` for each genre across different years.