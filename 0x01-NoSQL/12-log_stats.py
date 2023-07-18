#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']


def stat(mongo_collection, method=None):
    """Main function for stats generation"""
    items = {}
    if method:
        value = mongo_collection.count_documents(
            {"method": {"$regex": method}})
        print(f"\tmethod {method}: {value}")
        return
        
    res = mongo_collection.count_documents(items)
    print(f"{res} logs")
    print("methods:")
    for method in METHODS:
        stat(nginx_collection, method)
    status = mongo_collection.count_documents({"path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://localhost:27017').logs.nginx
    stat(nginx_collection)