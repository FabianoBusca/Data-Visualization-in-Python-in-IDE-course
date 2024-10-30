import unittest
import pandas as pd

from task import highest_rated_game


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


class TestCase(unittest.TestCase):
    def test_highest_rated_psv(self):
        data = load_dataset("../../../common/resources/data/dataset.csv")
        self.assertEqual(highest_rated_game(data), "LEGO Ninjago: Shadow of Ronin", msg="Finds the highest-rated game for the platform PSV and year "
                                                          "of release 2015")
