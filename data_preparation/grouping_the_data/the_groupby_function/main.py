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

    # Group the data by both 'platform' and 'genre'
    grouped_data = data.groupby(["platform", "genre"])

    # Calculate the average user count per group
    avg_rating = grouped_data["user_count"].mean()

    # Print the average user count per group
    print("Average rating per platform and genre:")
    print(avg_rating)
