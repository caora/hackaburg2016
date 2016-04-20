from pymongo import MongoClient
import time
import collections
import json
import unicodedata

# __init__() method is not necessary for use - therefore we ignore that warning here
class CreateDebate:

    def main_Method(self, request):

        self.is_Not_Used()

        try:
            if request.method == 'POST':
                request = json.loads(request.data)
                # connect to database
                mongo_DB_Client_Instance = MongoClient('mongodb://ds013290.mlab.com', 13290)
                mongo_DB_Instance = mongo_DB_Client_Instance["heroku_lzs554jn"]
                mongo_DB_Instance.authenticate('admin', 'admin')
                mongo_DB_Collection = mongo_DB_Instance.collection_names()

                # get data from request post context
                title = unicodedata.normalize('NFKD', request[u'title']).encode('ascii','ignore')
                self_text = unicodedata.normalize('NFKD', request[u'selftext']).encode('ascii','ignore')
                pro_text = unicodedata.normalize('NFKD', request[u'pro']).encode('ascii','ignore')
                con_text = unicodedata.normalize('NFKD', request[u'con']).encode('ascii','ignore')
                author = unicodedata.normalize('NFKD', request[u'author']).encode('ascii','ignore')

                self.write_Data_To_DB(author, title, self_text, pro_text, con_text, mongo_DB_Instance, mongo_DB_Collection)

                return "SUCCESS"
        except:

            return "FAIL"

    def is_Not_Used(self):

        pass

    def write_Data_To_DB(self, author, title, self_text, pro_text, con_text, mongo_DB_Instance, mongo_DB_Collection):

        new_debate_int = 0

        # The dict which is about to be written into the database
        dict_to_write_into_db = {
            "author": author,
            "created_utc": time.time(),
            "downs": 0,
            "ups": 0,
            "comment_id": 0,
            "title": title,
            "self_text": self_text,
            "pro_text": pro_text,
            "con_text": con_text
        }

        dict_to_write_into_db_vote = {
            "debate_id": None,
            "created_utc": None,
            "comment_id": None,
            "state": None,
            "user_id": None
        }

        # Iterates over every collection within the database
        for i in mongo_DB_Collection:

            # Whenever "debate" is in the name, get that last value
            if "debate" in i and "vote" not in i:
                name = str(i)
                integer_of_debate = name[7:]
                integer_of_debate = int(integer_of_debate)

                # Whenever the number of the iterated debate is higher than the actually one
                if integer_of_debate > new_debate_int:
                    new_debate_int = integer_of_debate

        # Need to raise that int by one, so that the new debate gets the appropriate id
        new_debate_int += 1

        # Writes the crawled information into the mongoDB
        collection = mongo_DB_Instance['debate_' + str(new_debate_int)]
        collectionVote = mongo_DB_Instance['debate_' + str(new_debate_int) + "_vote"]

        # Sorts the dictionary which is to be written, alphabetically correct
        dict_to_write_into_db = collections.OrderedDict(sorted(dict_to_write_into_db.items()))

        # Write the dictionary "data_to_write_into_db" into the mongo db right now!
        collection.insert_one(dict_to_write_into_db)
        collectionVote.insert_one(dict_to_write_into_db_vote)

        pass