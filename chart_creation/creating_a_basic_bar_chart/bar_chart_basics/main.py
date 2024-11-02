import pandas as pd
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


if __name__ == "__main__":
    # Path to the CSV file
    dataset_path = "../../../common/resources/data/dataset.csv"

    # Load the dataset
    data = load_dataset(dataset_path)

    # Plot a basic bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(data["year_of_release"], data["global_sales"], color="skyblue")
    plt.xlabel("Year of Release")
    plt.ylabel("Global sales")
    plt.title("Global Sales by Year of Release")
    plt.show()
