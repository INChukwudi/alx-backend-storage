#!/usr/bin/env python3

"""
File bearing the get_page function
also bears its related decorator
"""

import requests
import redis
import time
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def cache_content_and_count_calls(method: Callable):
    """decorator to cach content and count the calls"""
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        method the handles the method execution
        """
        redis_client.incr("count:{}".format(url))
        cached_result = redis_client.get("cached:{}".format(url))
        if cached_result:
            return cached_result.decode('utf-8')

        response = method(url)
        content = response.text

        redis_client.set("cached:{}".format(url), content, ex=10)

        return content

    return wrapper


@cache_content_and_count_calls
def get_page(url: str) -> str:
    """
    function to get a html page
    """
    return requests.get(url)
