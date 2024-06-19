#!/usr/bin/env python3
""" Function that uses request to obtain HTML content of a particular url"""
import requests
import redis
import time
from functools import wraps


# Initialize Redis client
redis_client = redis.Redis()


def count_calls_and_cache(func):
    """
    Decorator function to count the number of times a URL is accessed
    and cache the result with an expiration time of 10 seconds.

    Args:
        func (Callable): Function to decorate.

    Returns:
        Callable: Decorated function.
    """
    @wraps(func)
    def wrapper(url):
        # Increment the count of URL accesses
        redis_client.incr(f"count:{url}")

        # Check if the content is already cached
        cached_content = redis_client.get(url)
        if cached_content:
            return cached_content.decode()

        # Call the original function to fetch the content
        content = func(url)

        # Cache the content with expiration time of 10 seconds
        redis_client.setex(url, 10, content)

        return content

    return wrapper


@count_calls_and_cache
def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a given URL.

    Args:
        url (str): The URL of the web page.

    Returns:
        str: The HTML content of the web page.
    """
    # Simulate a slow response for testing
    if "slowwly.robertomurray.co.uk" in url:
        time.sleep(5)  # Simulate a delay of 5 seconds

    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error fetching URL: {url}. Status code: {
          response.status_code}"
