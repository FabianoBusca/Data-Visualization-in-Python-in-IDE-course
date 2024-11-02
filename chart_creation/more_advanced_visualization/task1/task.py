import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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


def create_grouped_bar_chart():
    # Path to the CSV file
    dataset_path = "../../../common/resources/data/dataset.csv"

    # Load the dataset
    data = load_dataset(dataset_path)

    # Fill NaN values
    ### YOUR CODE HERE ###



    ######################

    # Sort the years in ascending order
    ### YOUR CODE HERE ###



    ######################

    # Set the visual style
    sns.set(style="darkgrid")

    # Create the grouped bar chart
    plt.figure(figsize=(10, 6))
    ### YOUR CODE HERE ###



    ######################

    # Customize the chart
    ### YOUR CODE HERE ###



    ######################

    # Adjust layout to fit all elements
    plt.tight_layout()
    plt.show()

    # Return the DataFrame
    return data
