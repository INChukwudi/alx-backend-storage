#!/usr/bin/env python3

"""
File containing top_students function
"""


def top_students(mongo_collection):
    """
    Function that returns all students sorted by average score
    """
    students_docs = mongo_collection.find()
    students_info = []

    for doc in students_docs:
        topics = doc["topics"]

        total_score = sum(topic["score"] for topic in topics)
        average_score = total_score / len(topics)

        student_info = {
            "_id": doc["_id"],
            "name": doc["name"],
            "averageScore": average_score
        }

        students_info.append(student_info)

    students_info = sorted(
      students_info, key=lambda x: x["averageScore"], reverse=True)

    return students_info
