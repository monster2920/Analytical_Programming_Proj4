import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import random
import re


class SiteMapCollector:
    """
    A class to parse and collect sitemap URLs from a specified base website.

    Attributes:
        base_site (str): The base URL of the website to scrape.
        collected_data (dict): A dictionary holding sitemap URLs and their corresponding DataFrames.
        sitemap_count (int): A counter for the number of processed sitemaps.
        max_sitemaps (int): The maximum number of sitemaps to process.
        agents (list): A list of user agents for HTTP request headers.
    """

    def __init__(self, base_site, max_sitemaps=10, agents=None):
        """
        Initializes the SiteMapCollector with a base URL and optional limits and user agents.

        Args:
            base_site (str): The base URL of the website to parse.
            max_sitemaps (int): The maximum number of sitemaps to process.
            agents (list): A list of user agents for HTTP request headers.
        """
        self.base_site = base_site
        self.collected_data = {}
        self.sitemap_count = 0
        self.max_sitemaps = max_sitemaps
        self.agents = agents or [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
            # Add more user agents if necessary
        ]
        self._search_sitemaps()

    def _request_content(self, url):
        """
        Sends a HTTP GET request to the specified URL.

        Args:
            url (str): The URL to send the request to.

        Returns:
            str: The content of the response.
        """
        headers = {"User-Agent": random.choice(self.agents)}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException:
            return ""

    def _parse_sitemap(self, sitemap_url):
        """
        Parses the sitemap at the given URL.

        Args:
            sitemap_url (str): The URL of the sitemap to parse.
        """
        if self.sitemap_count >= self.max_sitemaps:
            return

        xml_content = self._request_content(sitemap_url)
        found_urls = self._extract_links(xml_content)

        for link in found_urls:
            if re.search(r"\.xml$", link) and self.sitemap_count < self.max_sitemaps:
                self.sitemap_count += 1
                self._parse_sitemap(link)

        self.collected_data[sitemap_url] = pd.DataFrame(found_urls, columns=["URLs"])

    def _extract_links(self, xml_content):
        """
        Extracts URLs from the XML content.

        Args:
            xml_content (str): The XML content to parse.

        Returns:
            list: A list of extracted URLs.
        """
        soup = BeautifulSoup(xml_content, "xml")
        return [loc.text for loc in soup.find_all("loc")]

    def _search_sitemaps(self):
        """
        Searches for and processes sitemaps from the robots.txt file of the base site.
        """
        robots_content = self._request_content(f"{self.base_site}/robots.txt")
        for line in robots_content.splitlines():
            if line.startswith("Sitemap:"):
                sitemap_link = line.split(": ")[1].strip()
                if self.sitemap_count < self.max_sitemaps:
                    self.sitemap_count += 1
                    self._parse_sitemap(sitemap_link)

    def filter_urls(self):
        """
        Refines the URLs by extracting subdirectories and updating the DataFrames.
        """
        for _, df in self.collected_data.items():
            df["Subdirectories"] = df["URLs"].apply(
                lambda x: x.replace(f"{self.base_site}/", "").split("/")
            )

    def save_csv(self, folder="sitemap_files"):
        """
        Saves the collected sitemap URLs to CSV files.

        Args:
            folder (str): The directory to save the CSV files.
        """
        if not os.path.exists(folder):
            os.makedirs(folder)

        for key, df in self.collected_data.items():
            file_name = f"{folder}/{key.split('/')[-1]}.csv"
            df.to_csv(file_name, index=False)
