## Objective
In this task, you will learn how to perform basic exploration of a dataset in Python using `pandas`. Understanding these foundational commands will help you get an overview of the dataset structure, summary statistics, and specific values.

## Commands for Basic Exploration

1. **Viewing Columns**  
   To view the list of column names in a dataset:
   ```python
   data.columns
   ```
   This command is helpful for identifying the data structure and column names available.

2. **Descriptive Statistics**  
   Use `.describe()` to get an overview of summary statistics for each numerical column:
   ```python
   data.describe()
   ```
   This command provides statistics like mean, standard deviation, minimum, maximum, and percentiles.

3. **Viewing Specific Columns**  
   To view a single column:
   ```python
   data['ColumnName']
   ```
   To view multiple columns:
   ```python
   data[['Column1', 'Column2']]
   ```
   This lets you isolate columns of interest for more targeted analysis.

4. **Filtering Data**  
   To filter rows based on a condition, such as all rows where the value in `ColumnName` is greater than a certain number:
   ```python
   data[data['ColumnName'] > some_value]
