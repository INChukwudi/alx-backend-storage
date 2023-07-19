#!/usr/bin/env python3
"""
File containing the schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns the list of school having a specific topic
    """
    schools = list(mongo_collection.find({"topics": {"$in": [topic]}}))
    return schools
