import pandas as pd

def load_dataset(dataset_path):
    """
    Loads a dataset from the specified CSV file path and prints the first few rows.

    Args:
    - dataset_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The loaded DataFrame object.
    """
    try:
        # Load the dataset
        data = pd.read_csv(dataset_path)

        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_pivot_table():
    """
    Creates a pivot table with genre and user_count.
    :return: The pivot table.
    """
    # Path to the CSV file
    dataset_path = "../../../common/resources/data/dataset.csv"

    # Load the dataset
    data = load_dataset(dataset_path)

    # Fill NaN values in user_count
    ### YOUR CODE HERE ###



    ######################

    # Create a pivot table with genre and year_of_release
    ### YOUR CODE HERE ###

    pivot_table =

    ######################

    # Print the pivot table and analyze
    print("\nPivot Table by Genre and User Count:\n\n", pivot_table)

    # Return the pivot table
    return pivot_table
