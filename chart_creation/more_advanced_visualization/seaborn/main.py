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


if __name__ == "__main__":
    # Path to the CSV file
    dataset_path = "../../../common/resources/data/dataset.csv"

    # Load the dataset
    data = load_dataset(dataset_path)

    # Filter the dataset to include only some platforms
    data = data[data['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]

    # Fill NaN values in 'genre' and 'platform' columns (if any)
    data['genre'] = data['genre'].fillna('Unknown')
    data['platform'] = data['platform'].fillna('Unknown')

    # Sort the genres alphabetically
    data['genre'] = pd.Categorical(data['genre'], categories=sorted(data['genre'].unique()))

    # Set the visual style
    sns.set(style="darkgrid")

    # Create the grouped bar chart
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x="platform", hue="genre", palette="husl", order=['PS4', 'XOne', 'PC', 'WiiU'])

    # Customize the chart
    plt.xlabel("Platform")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.legend(title="Genre", bbox_to_anchor=(1, 0.75), loc='upper left', frameon=False)

    # Adjust layout to fit all elements
    plt.tight_layout()
    plt.show()
