import unittest
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.testing import assert_frame_equal

from task import create_grouped_bar_chart, load_dataset


def answer():
    # Path to the CSV file
    dataset_path = "../../../common/resources/data/dataset.csv"

    # Load the dataset
    data = load_dataset(dataset_path)

    # Fill NaN values
    ### YOUR CODE HERE ###

    data['rating'] = data['rating'].fillna('Unknown')

    ######################

    # Sort the years in ascending order
    ### YOUR CODE HERE ###

    data['rating'] = pd.Categorical(data['rating'], categories=sorted(data['rating'].unique()))

    ######################

    # Set the visual style
    sns.set(style="darkgrid")

    # Create the grouped bar chart
    plt.figure(figsize=(10, 6))
    ### YOUR CODE HERE ###

    sns.countplot(data=data, x="year_of_release", hue="rating", palette="husl")

    ######################

    # Customize the chart
    ### YOUR CODE HERE ###

    plt.xlabel("Year of Release")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.legend(title="Rating", bbox_to_anchor=(1, 0.75), loc='upper left', frameon=False)

    ######################

    # Adjust layout to fit all elements
    plt.tight_layout()
    plt.show()

    # Return the DataFrame
    return data

class TestCase(unittest.TestCase):
    def test_add(self):
        assert_frame_equal(create_grouped_bar_chart(), answer())
