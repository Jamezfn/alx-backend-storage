#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
Displays total logs, count of each HTTP method, count of GET requests to /status,
and top 10 most frequent IPs.
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Analyzes Nginx logs in a MongoDB collection and prints statistics.
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = mongo_collection.aggregate(pipeline)
    print("IPs:")
    for ip_doc in top_ips:
        print(f"\t{ip_doc['_id']}: {ip_doc['count']}")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
    client.close()
