#!/usr/bin/env python

def update_topics(mongo_collection, name, topics):
    """Updates all documents in a MongoDB collection with the specified name,
    setting their topics field to the provided list of topics."""
    mongo_collection.update_many(
      {"name": name},
      {"$set": {"topics": topics}}
    )
