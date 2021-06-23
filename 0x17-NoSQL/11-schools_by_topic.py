#!/usr/bin/env python3
"""schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    list_all = mongo_collection.find({"topic": topic})
    return list_all
