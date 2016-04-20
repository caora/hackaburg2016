from pymongo import MongoClient
import collections
import time

mongo_DB_Client_Instance = MongoClient('mongodb://ds013290.mlab.com', 13290)
mongo_DB_Instance = mongo_DB_Client_Instance["heroku_lzs554jn"]
mongo_DB_Instance.authenticate('admin', 'admin')
mongo_DB_Collection = mongo_DB_Instance.collection_names()

# Test data is defined here for debate
test_dict = {
    "author": "Sepp",
    "created_utc": time.time(),
    "downs": 10,
    "ups": 11,
    "pro_text": "Ich bin dafuer",
    "con_text": "Ich bin dagegen",
    "comment_id": 1,
    #    "num_comments": 10,    # <<< kriegen wir anhand der collection.length()
    "title": "Ich bin ein Title",
    "selftext": "Ich weiss ned ob ich wichtig bin"
}

print("Bin davor")
# Source: http://www.avilpage.com/2014/11/python-unix-timestamp-utc-and-their.html
print(time.time())
print("Bin danach")
test_dict = collections.OrderedDict(sorted(test_dict.items()))

new_debate_int = 0

# Iterates over every collection within the database
for i in mongo_DB_Collection:

    # Whenever "debate" is in the name, get that last value
    if "debate" in i:
        name = str(i)
        integer_of_debate = name[7:]
        integer_of_debate = int(integer_of_debate)
        if integer_of_debate > new_debate_int:
            new_debate_int = integer_of_debate

        print(name)

# Need to raise that int by one, so that the new debate gets the appropriate id
new_debate_int += 1

print(type(new_debate_int))
print(str(new_debate_int))


# Writes the crawled information into the mongoDB
collection = mongo_DB_Instance['debate_' + str(new_debate_int)]

# Write the dictionary "data_to_write_into_db" into the mongo db right now!
collection.insert_one(test_dict)
