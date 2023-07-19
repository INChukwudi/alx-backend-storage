#!/usr/bin/env python3
"""
File containing the list_all function
"""


def list_all(mongo_collection):
    """
    Function that lists all documents in a collection

    Args:
    mongo_collection - collection from a mongoDb

    Return:
    value - list bearing the collection documents
    """
    documents = list(mongo_collection.find({}))
    return documents
