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

    # IPs sorting
    ip_count_dict = {}
    ips = nginx_collection.distinct("ip")
    for address in ips:
        ip_count = nginx_collection.count_documents({"ip": address})
        ip_count_dict[address] = ip_count

    sorted_ip_counts = dict(
      sorted(ip_count_dict.items(), key=lambda x: x[1], reverse=True)[:10])

    print("IPs:")
    for ip, count in sorted_ip_counts.items():
        print("\t{}: {}".format(ip, count))

    client.close()
