import unittest
import matplotlib.pyplot as plt
from pandas.testing import assert_frame_equal

from task import create_bar_chart, load_dataset


def answer():
    # Path to the CSV file
    dataset_path = "../../../common/resources/data/dataset.csv"

    # Load the dataset
    data = load_dataset(dataset_path)

    # Fill NaN values in user_count
    ### YOUR CODE HERE ###

    ######################

    data['user_count'] = data['user_count'].fillna(0)

    # Create a new DataFrame with the average user count by rating
    ### YOUR CODE HERE ###

    avg_user_count = data.groupby('rating')['user_count'].mean().reset_index()
    avg_user_count.columns = ['rating', 'avg_user_count']

    ######################

    plt.figure(figsize=(10, 6))
    # Plot the bar chart
    ### YOUR CODE HERE ###

    plt.bar(avg_user_count['rating'], avg_user_count['avg_user_count'], color='skyblue')

    ######################
    plt.xlabel('Rating')
    plt.ylabel('Average User Count')
    plt.title('Average User Count by Rating')
    plt.xticks(rotation=45)
    plt.show()

    # Return the DataFrame
    return avg_user_count

class TestCase(unittest.TestCase):
    def test_add(self):
        assert_frame_equal(create_bar_chart(), answer())
