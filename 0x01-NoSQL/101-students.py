#!/usr/bin/env python

from pymongo import MongoClient

def top_students(mongo_collection):
    """Returns all students sorted by average score in descending order."""
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
