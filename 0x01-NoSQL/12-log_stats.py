#!/usr/bin/env python3

"""
Script that provides some stats about Nginx logs stored in MongoDB:
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Total Logs
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # Methods and Method Count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))

    # Path Status Info
    status_count = nginx_collection.count_documents(
      {"method": "GET", "path": "/status"})
    print("{} status check".format(status_count))

    client.close()
