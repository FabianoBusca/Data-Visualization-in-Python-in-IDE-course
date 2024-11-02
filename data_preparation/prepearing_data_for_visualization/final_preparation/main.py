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

    # Load the dataset
    data = load_dataset(dataset_path)

    # Sort data by year of release and rating
    sorted_data = data.sort_values(by=["year_of_release", "rating"], ascending=[True, False])

    # Categorize ratings, setting an ordered category
    rating_order = pd.CategoricalDtype(['E', 'E10+', 'T', 'M', 'Unknown'], ordered=True)
    data['rating'] = data['rating'].astype(rating_order)

    # Replace NaNs in rating with 'Unknown'
    data['rating'] = data['rating'].fillna('Unknown')

    # Create a pivot table with 'genre' as rows and 'year_of_release' as columns
    pivot_data = data.pivot_table(values='name', index='genre', columns='year_of_release', aggfunc='count')

    print("\nSorted Data:\n", sorted_data.head())
    print("\nCategorized Ratings:\n", data['rating'].value_counts())
    print("\nPivot Table:\n", pivot_data.head())
