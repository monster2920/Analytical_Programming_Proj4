# web_scraping.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


class CountryScraper:
    """
    This class is used for scraping country-related data from a webpage. It takes a URL as input and scrapes data such as the country's name, capital, population, and area. The scraped data is returned in the form of a pandas DataFrame, which can then be saved to a CSV file.
    """

    def __init__(self, url: str):
        self.url = url

    def _fetch_data(self) -> BeautifulSoup:
        """
        Fetches and parses the HTML content from the webpage using requests and BeautifulSoup.

        Returns:
            BeautifulSoup object containing parsed HTML content.
        """

        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return BeautifulSoup(response.content, "html.parser")
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def scrape_country_data(self) -> pd.DataFrame:
        """
        Scrapes country data from the webpage using BeautifulSoup to find relevant HTML elements and extract the text content. The scraped data includes the name of the country, its capital city, population, and area. This method assumes a certain structure of the webpage and specific class names for the elements that contain the data.

        Returns:
            A pandas DataFrame with columns for country name, capital, population, and area.
        """

        soup = self._fetch_data()
        if soup is None:
            return (
                pd.DataFrame()
            )  # Return an empty DataFrame if we couldn't fetch the data

        country_divs = soup.find_all("div", class_="country")

        countries = []
        capitals = []
        populations = []
        areas = []

        for div in country_divs:
            countries.append(div.find("h3", class_="country-name").get_text(strip=True))
            capitals.append(
                div.find("span", class_="country-capital").get_text(strip=True)
            )
            populations.append(
                div.find("span", class_="country-population").get_text(strip=True)
            )
            areas.append(div.find("span", class_="country-area").get_text(strip=True))

        return pd.DataFrame(
            {
                "Country": countries,
                "Capital": capitals,
                "Population": populations,
                "Area": areas,
            }
        )

    def save_to_csv(self, filename: str):
        """
        Saves the scraped country data into a CSV file with the given filename.

        Parameters:
            filename (str): The filename for the CSV file where the data will be saved.
        """

        country_data = self.scrape_country_data()
        if not country_data.empty:
            country_data.to_csv(filename, index=False)
            print(f"Data saved to {filename}")
        else:
            print("No data to save.")


class WebScraper:
    """
    This class is used for scraping tabular data from web pages. It can handle pagination and compiles data from multiple pages into a single pandas DataFrame. The class is generic and can be used for any website that has a similar tabular structure with pagination.

    Attributes:
        base_url (str): The base URL used for constructing complete URLs.
n   Methods:
        __init__(self, base_url: str): Initializes the DataFetcher instance with a base URL.
        _fetch_url(self, url: str) -> str: Fetches data from the provided URL and returns the response text.
    
    """

    def __init__(self, base_url: str):
        """
        Initializes the DataFetcher instance with a base URL.

        Parameters:
            base_url (str): The base URL used for constructing complete URLs.
        """
        self.base_url = base_url

    def _fetch_url(self, url: str) -> str:
        """
        Fetches data from the provided URL and returns the response text.

        Parameters:
            url (str): The complete URL for data retrieval.

        Returns:
            str: The response text if successful, an empty string otherwise.
        """
        try:
            with requests.get(url) as response:
                response.raise_for_status()
                return response.text
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return ""
        except Exception as err:
            print(f"An error occurred: {err}")
            return ""

    def _extract_pagination_links(self, content: str) -> list[str]:
        """
    Extracts pagination links from HTML content.

    Parameters:
        content (str): The HTML content containing pagination links.

    Returns:
        list[str]: A list of complete pagination URLs based on the base URL.
                   An empty list is returned if no pagination links are found.
    """
        soup = BeautifulSoup(content, "html.parser")
        pagination_div = soup.find("div", class_="pagination")
        if not pagination_div:
            # If no pagination div found, return an empty list
            return []
        return [
            urljoin(self.base_url, a["href"])
            for a in pagination_div.find_all("a")
            if "page_num=" in a.get("href", "")
        ]

    def _extract_table_data(self, content: str) -> pd.DataFrame:

         """
    Extracts tabular data from HTML content and returns it as a Pandas DataFrame.

    Parameters:
        content (str): The HTML content containing the table data.

    Returns:
        pd.DataFrame: A DataFrame representing the tabular data. 
                      If no table is found, an empty DataFrame is returned.
    """
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find("table")
        if table is None:
            # If no table found, return an empty DataFrame
            return pd.DataFrame()

        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        rows = [
            [td.get_text(strip=True) for td in tr.find_all("td")]
            for tr in table.find_all("tr")
            if tr.find("td")
        ]
        return pd.DataFrame(rows, columns=headers)

    def scrape_data(self, url: str) -> pd.DataFrame:
        """
        Coordinates the scraping process by fetching the initial page, extracting any pagination links, and then iterating over all pages to scrape the table data. The extracted data from all pages is combined into a single DataFrame.

        Parameters:
            url (str): The URL where the table data starts, typically the first page of a paginated table.

        Returns:
            A pandas DataFrame containing the combined data from all pages.
        """

        content = self._fetch_url(url)
        if not content:
            return (
                pd.DataFrame()
            )  # Return an empty DataFrame if we couldn't fetch the content

        pagination_links = self._extract_pagination_links(content)
        all_data = [self._extract_table_data(content)]
        for link in pagination_links:
            page_content = self._fetch_url(link)
            if page_content:
                all_data.append(self._extract_table_data(page_content))

        return pd.concat(all_data, ignore_index=True)

    def save_to_csv(self, filename: str):
        """
        Saves the scraped tabular data into a CSV file. It calls the scrape_data method to get the data and then saves it to a CSV file with the given filename.

        Parameters:
            filename (str): The filename for the CSV file where the data will be saved.
        """

        data = self.scrape_data(self.base_url)
        if not data.empty:
            data.to_csv(filename, index=False)
            print(f"Data saved to {filename}")
        else:
            print("No data to save.")

    # Add these methods to the WebScraper class

    def calculate_win_percentages(self, df):
        """
        Calculate win percentages for each team and add it as a new column to the DataFrame.

        Parameters:
            df (pd.DataFrame): The DataFrame containing the teams' data.

        Returns:
        pd.DataFrame: The DataFrame with the win percentage column added.
        """
        df["Win %"] = df["Wins"] / (df["Wins"] + df["Losses"])
        return df

    def top_performing_teams(self, df, year):
        """
        Identify the top performing teams for a given year based on win percentage.

        Parameters:
            df (pd.DataFrame): The DataFrame containing the teams' data.
            year (str): The year to filter the data on, as a string.

        Returns:
            pd.DataFrame: The DataFrame containing only the data for the top teams in the specified year.
        """
        # Ensure that the year is a string since the unique values showed 'Year' as an object
        df_year = df[df["Year"] == year]

        # Add a print statement to see if the filtering is working
        print(f"Filtered DataFrame for year {year} has {len(df_year)} rows")

        # Sort the DataFrame by 'Win %' column
        df_year_sorted = df_year.sort_values(by="Win %", ascending=False)

        # Return the top 5 entries
        return df_year_sorted.head()
