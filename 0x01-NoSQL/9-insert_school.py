#!/usr/bin/env python

def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a MongoDB collection based on kwargs."""
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
