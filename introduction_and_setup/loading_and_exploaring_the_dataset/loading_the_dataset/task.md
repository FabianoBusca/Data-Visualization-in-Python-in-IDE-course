## Objective
In this lesson, we will learn how to load a dataset in Python using the `pandas` library. This knowledge is essential for data analysis and visualization, as `pandas` allows us to handle data in tabular form efficiently.

## What is `pandas`?
`Pandas` is a powerful library in Python for data manipulation and analysis. It provides a `DataFrame` structure, which is similar to a table or spreadsheet and makes it easy to read, manipulate, and analyze data.

## Reading a Dataset
To read data into a `DataFrame`, `pandas` provides a function called `read_csv()`. This function can load data from various file formats, including CSV (Comma-Separated Values), Excel files, SQL databases, and more.

## Syntax for Loading a CSV File
To load a dataset from a CSV file, use the following syntax:

```python
import pandas as pd

# Load the dataset
data = pd.read_csv('dataset_path.csv')

# Display the first few rows of the dataset
print(data.head())
```