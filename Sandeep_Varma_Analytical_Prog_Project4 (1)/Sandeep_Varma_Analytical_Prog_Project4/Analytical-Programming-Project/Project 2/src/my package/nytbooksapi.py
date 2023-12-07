import requests
import pandas as pd
import time


class NYTBooksAPI:
    """
    A class to interface with the New York Times Books API.

    Attributes:
        api_key (str): The API key for authenticating requests to the NYT API.
        base_url (str): The base URL for the NYT Books API.
    """

    def __init__(self, api_key):
        """
        Initializes the NYTBooksAPI with the provided API key.

        Args:
            api_key (str): The API key for authenticating requests to the NYT API.
        """
        self.api_key = api_key
        self.base_url = "https://api.nytimes.com/svc/books/v3/lists/current/"

    def fetch_data(self, category):
        """
        Fetches the book data for a given category from the NYT Books API.

        Args:
            category (str): The category of books to fetch data for.

        Returns:
            dict: A dictionary of the JSON response from the API.
        """
        url = f"{self.base_url}{category}.json?api-key={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            time.sleep(1)  # Sleep for a second to respect rate limits
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def aggregate_data(self, categories):
        """
        Aggregates the book data for multiple categories into a pandas DataFrame.

        Args:
            categories (list): A list of categories to fetch book data for.

        Returns:
            DataFrame: A pandas DataFrame containing the aggregated book data.
        """
        data_frames = []
        for category in categories:
            data = self.fetch_data(category)
            if data and "results" in data and "books" in data["results"]:
                books = data["results"]["books"]
                for book in books:
                    book["category"] = category  # Add category as a column
                data_frames.extend(books)
        return pd.DataFrame(data_frames)


# The usage example should be outside of the class and typically would not be included in the module file.
