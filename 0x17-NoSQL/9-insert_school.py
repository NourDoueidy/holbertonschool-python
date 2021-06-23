#!/usr/bin/env python3
"""insert in pymongo"""


def insert_school(mongo_collecion, **kwargs):
    """Function that inserts a new document in a collection based on kwargs"""
    ins_doc = mongo_collection.insert(kwargs)
    return ins_doc
