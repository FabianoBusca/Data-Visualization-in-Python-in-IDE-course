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


if __name__ == "__main__":
    # Path to the CSV file
    dataset_path = "../../../common/resources/data/dataset.csv"

    # Load and preview the dataset
    data = load_dataset(dataset_path)

    # Display columns
    print("Columns: [")
    for column in data.columns:
        print(f"\t'{column}',")
    print("]")

    # Show summary statistics
    print(data.describe())

    # Extract specific columns
    print("Extracted columns:")
    print(data[['name', 'platform']])

    # Filter rows based on a condition
    print("Games released in 2017:")
    print(data[data['year_of_release'] == 2017])
