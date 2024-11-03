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


def create_bar_chart():
    """
    Creates a bar chart showing the average user count by rating.
    :return: The DataFrame with the average user count by rating.
    """
    # Path to the CSV file
    dataset_path = "../../../common/resources/data/dataset.csv"

    # Load the dataset
    data = load_dataset(dataset_path)

    # Fill NaN values in user_count
    ### YOUR CODE HERE ###



    ######################

    # Create a new DataFrame with the average user count by rating
    ### YOUR CODE HERE ###

    avg_user_count =

    ######################

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    ### YOUR CODE HERE ###

    plt.bar()

    ######################
    plt.xlabel('Rating')
    plt.ylabel('Average User Count')
    plt.title('Average User Count by Rating')
    plt.xticks(rotation=45)
    plt.show()

    # Return the DataFrame
    return avg_user_count
