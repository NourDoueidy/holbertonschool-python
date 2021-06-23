#!/usr/bin/env python3
"""insert in pymongo"""


def insert_school(mongo_collecTion, **kwargs):
    """Function that inserts a new document in a collection based on kwargs"""
    document_id = mongo_collection.insert(kwargs)
    return document_id
