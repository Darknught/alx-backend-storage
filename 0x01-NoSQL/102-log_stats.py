#!/usr/bin/env python3
""" A Script that provides stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def nginx_stats():
    """ The function to execute the script.
    Added top 10 sorted present IPs in the collection
    """
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Connect to the database and collection
    db = client['logs']
    collection = db['nginx']

    # get the number of documents in the collection
    total_logs = collection.count_documents({})

    # Print the total number of logs
    print(f"{total_logs} logs")

    # Print the method stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Print the number of documents with method GET and path / status
    stats_check = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{stats_check} status check ")

    # Top 10 most present IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(collection.aggregate(pipeline))

    # Print the top 10 most present IPs
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    nginx_stats()
