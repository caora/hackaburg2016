from pymongo import MongoClient
import time
import collections
import json
import unicodedata

# __init__() method is not necessary for use - therefore we ignore that warning here
class CreateComment:

    def main_Method(self, request):

        self.is_Not_Used()

        try:
            if request.method == 'POST':
                request = json.loads(request.data)

                # connect to database
                mongo_DB_Client_Instance = MongoClient('mongodb://ds013290.mlab.com', 13290)
                mongo_DB_Instance = mongo_DB_Client_Instance["heroku_lzs554jn"]
                mongo_DB_Instance.authenticate('admin', 'admin')
                debate = unicodedata.normalize('NFKD', request[u'debate']).encode('ascii','ignore')
                mongo_DB_Requested_Thread = mongo_DB_Instance[debate]
                mongo_DB_Requested_Thread_Cursor = mongo_DB_Requested_Thread.find()

                # get data from request post context
                title = unicodedata.normalize('NFKD', request[u'title']).encode('ascii','ignore')
                text = unicodedata.normalize('NFKD', request[u'text']).encode('ascii','ignore')
                state = unicodedata.normalize('NFKD', request[u'state']).encode('ascii','ignore')
                author = unicodedata.normalize('NFKD', request[u'author']).encode('ascii','ignore')

                self.write_Data_To_DB(author, title, text, state, mongo_DB_Requested_Thread, mongo_DB_Requested_Thread_Cursor)

                return "SUCCESS"
        except:
            return "FAIL"

    def is_Not_Used(self):

        pass

    def write_Data_To_DB(self, author, title, text, state, mongo_DB_Requested_Thread, mongo_DB_Requested_Thread_Cursor):

        # The id for the newly generated comment
        new_comment_id_int = 0
        pro_text = ""
        con_text = ""

        if state == "pro":
            pro_text = text
        else:
            con_text = text

        # Iterates over all comments within the collection
        for i in mongo_DB_Requested_Thread_Cursor:

            # Gets the current id of the actually iterated comment
            current_comment_id_int = i['comment_id']

            # If the id of the actually iterated comment is higher than the curent ones
            if current_comment_id_int > new_comment_id_int:
                new_comment_id_int = current_comment_id_int

        # Raise by one for the new comment
        new_comment_id_int += 1

        # Test data is defined here for debate
        dict_to_write_into_db = {
            "author": author,
            "created_utc": time.time(),
            "downs": 0,
            "ups": 0,
            "pro_text": pro_text,
            "con_text": con_text,
            "comment_id": new_comment_id_int,
            "title": title,
        }

        # Sorts the dictionary which is to be written, alphabetically correct
        dict_to_write_into_db = collections.OrderedDict(sorted(dict_to_write_into_db.items()))

        # Write the dictionary "data_to_write_into_db" into the mongo db right now!
        mongo_DB_Requested_Thread.insert_one(dict_to_write_into_db)

        pass