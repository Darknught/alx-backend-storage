#!/usr/bin/env python3
""" Function that uses request to obtain HTML content of a particular url"""
import requests
import redis
import time


# Initialize Redis client
redis_client = redis.Redis()

def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a given URL, caches it in Redis with an expiration time of 10 seconds,
    and counts the number of accesses to the URL.

    Args:
        url (str): The URL of the web page.

    Returns:
        str: The HTML content of the web page.
    """
    # Increment the count of URL accesses
    redis_client.incr(f"count:{url}")

    # Check if the content is already cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode()

    # Simulate a slow response for testing
    if "slowwly.robertomurray.co.uk" in url:
        time.sleep(5)  # Simulate a delay of 5 seconds

    # Fetch the content from the URL
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        # Cache the content with expiration time of 10 seconds
        redis_client.setex(url, 10, content)
        return content
    else:
        return f"Error fetching URL: {url}. Status code: {response.status_code}"
