from pymongo import MongoClient
import collections
import time

mongo_DB_Client_Instance = MongoClient('mongodb://ds013290.mlab.com', 13290)
mongo_DB_Instance = mongo_DB_Client_Instance["heroku_lzs554jn"]
mongo_DB_Instance.authenticate('admin', 'admin')
mongo_DB_Requested_Thread = mongo_DB_Instance['debate_1']
mongo_DB_Requested_Thread_Cursor = mongo_DB_Requested_Thread.find()

new_comment_id_int = 0

# Iterates over all comments within the collection
for i in mongo_DB_Requested_Thread_Cursor:

    # Gets the current id of the actually iterated comment
    current_comment_id_int = i['comment_id']

    # If the id of the actually iterated comment is higher than the curent ones
    if current_comment_id_int > new_comment_id_int:
        new_comment_int = current_comment_id_int

# Raise by one for the new comment
new_comment_id_int += 1

# Test data is defined here for debate
test_dict = {
    "author": "Sepp_2",
    "created_utc": time.time(),
    "downs": 0,
    "ups": 0,
    "pro_text": "Ich bin dafuer",
    "con_text": "",
    "comment_id": new_comment_id_int,
    "title": "Ich bin ein Title",
    "selftext": "Ich weiss ned ob ich wichtig bin"
}

test_dict = collections.OrderedDict(sorted(test_dict.items()))

mongo_DB_Requested_Thread.insert_one(test_dict)
