#!/usr/bin/env python

def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection."""
    return list(mongo_collection.find())
