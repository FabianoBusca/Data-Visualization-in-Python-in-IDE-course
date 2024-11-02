## Objective
In this lesson, we’ll cover essential data transformation techniques to prepare our dataset for visualization, focusing on sorting, categorizing, and pivoting data for structured charts. Handling categorical values, like game ratings, can help ensure that the data is organized consistently for meaningful visualizations.

## Concepts Covered

1. **Sorting**:
   - Sorting data allows us to order entries based on one or more columns. For example, sorting by `year_of_release` and `rating` can help us see trends and distribution.

2. **Handling Categorical Data**:
   - Categorical columns like `rating` may contain specific categories that aren’t numerical. Encoding or categorizing these values can help ensure they’re consistently handled.
   - In this case, we’ll convert the ratings to an ordered categorical type to organize them in a defined order, making charts easier to interpret.

3. **Pivoting**:
   - Pivoting reorganizes data into a tabular format, making it easier to compare across categories like `year_of_release` and `genre`.
   - Example: Creating a pivot table with `genre` as rows and `year_of_release` as columns allows us to see genre distributions over time.
