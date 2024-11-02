import unittest
from pandas.testing import assert_frame_equal

from task import create_pivot_table, load_dataset


def answer():
    # Path to the CSV file
    dataset_path = "../../../common/resources/data/dataset.csv"

    # Load the dataset
    data = load_dataset(dataset_path)

    # Fill NaN values in user_count
    ### YOUR CODE HERE ###

    data["user_count"] = data["user_count"].fillna(0)

    ######################

    # Create a pivot table with genre and year_of_release
    ### YOUR CODE HERE ###

    pivot_table = data.pivot_table(index="genre", columns="year_of_release", values="user_count", aggfunc="sum")

    ######################

    # Print the pivot table and analyze
    print("\nPivot Table by Genre and User Count:\n\n", pivot_table)

    # Return the pivot table
    return pivot_table


class TestCase(unittest.TestCase):
    def test_add(self):
        assert_frame_equal(create_pivot_table(), answer())
