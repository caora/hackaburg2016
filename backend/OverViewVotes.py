from pymongo import MongoClient
import simplejson

# __init__() method is not necessary for use - therefore we ignore that warning here
class OverViewVotes:

    def main_Method(self):

        self.is_Not_Used()

        #connect to database
        mongo_DB_Client_Instance = MongoClient('mongodb://ds013290.mlab.com', 13290)
        mongo_DB_Instance = mongo_DB_Client_Instance["heroku_lzs554jn"]
        mongo_DB_Instance.authenticate('admin', 'admin')

        for collection in mongo_DB_Instance.collection_names():
            # Only affects debates (running discussions)
            if 'debate' in collection and 'vote' not in collection and 'closed' not in collection:
                collectionDebate = mongo_DB_Instance[collection]

                # The id of the initial post - necessary for mongo db updating
                sys_id_of_entry_thread = None

                amount_of_pro_comments = 0
                amount_of_con_comments = 0

                # Iterates over every document (comment) within the collection (thread / debate)
                for i, entry in enumerate(collectionDebate.find()):
                    # Whenever it is the initial post ( starting post )
                    if i == 0:
                        sys_id_of_entry_thread = entry.get("_id")

                    else:
                        if entry['pro_text'] != "":
                            amount_of_pro_comments += 1

                        elif entry['con_text'] != "":
                            amount_of_con_comments += 1

                        else:
                            pass

                #  print(collection, sys_id_of_entry_thread, amount_of_pro_comments, amount_of_con_comments)
                actual_debate_collection = mongo_DB_Instance[str(collection)]
                actual_debate_collection.update_one({
                    '_id': sys_id_of_entry_thread
                }, {
                    '$set': {"ups": amount_of_pro_comments,
                             "downs": amount_of_con_comments}
                }, upsert=False)

    def is_Not_Used(self):
        pass