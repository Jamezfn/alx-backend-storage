#!/usr/bin/env python

def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools having a specific topic in their topics field."""
    return list(mongo_collection.find({"topics": topic}))
