from pymongo import MongoClient
import time
import collections

# __init__() method is not necessary for use - therefore we ignore that warning here
class CommentVote:

    def main_Method(self, request):

        self.is_Not_Used()

        try:
            if request.method == 'POST':

                # connect to database
                mongo_DB_Client_Instance = MongoClient('mongodb://ds013290.mlab.com', 13290)
                mongo_DB_Instance = mongo_DB_Client_Instance["heroku_lzs554jn"]
                mongo_DB_Instance.authenticate('admin', 'admin')

                # get data from request post context
                debate_id = request.form['debate_id']
                comment_id = request.form['comment_id']
                state = request.form['state']
                user_id = request.form['user_id']

                self.write_Data_To_DB(debate_id, comment_id, state, user_id, user_id, mongo_DB_Instance)

                return "SUCCESS"
        except:

            return "FAIL"

    def is_Not_Used(self):

        pass

    def write_Data_To_DB(self, debate_id, comment_id, state, user_id, mongo_DB_Instance):

        # The dict which is about to be written into the database
        dict_to_write_into_db = {
            "debate_id": debate_id,
            "created_utc": time.time(),
            "comment_id": comment_id,
            "state": state,
            "user_id": user_id
        }

        collection = mongo_DB_Instance[debate_id + "_vote"]

        # Sorts the dictionary which is to be written, alphabetically correct
        dict_to_write_into_db = collections.OrderedDict(sorted(dict_to_write_into_db.items()))

        # Write the dictionary "data_to_write_into_db" into the mongo db right now!
        collection.insert_one(dict_to_write_into_db)

        pass