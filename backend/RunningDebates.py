from pymongo import MongoClient
import simplejson

# __init__() method is not necessary for use - therefore we ignore that warning here
class RunningDebates:

    def main_Method(self):

        self.is_Not_Used()
        data = {}
        main_array = []

        # Connect to database
        mongo_DB_Client_Instance = MongoClient('mongodb://ds013290.mlab.com', 13290)
        mongo_DB_Instance = mongo_DB_Client_Instance["heroku_lzs554jn"]
        mongo_DB_Instance.authenticate('admin', 'admin')

        for collection in mongo_DB_Instance.collection_names():
            if 'debate' in collection and 'vote' not in collection and 'closed' not in collection:
                collection_debate = mongo_DB_Instance[collection]

                string_content = collection_debate.find()

                # Gets the current correct amount of comments / ups / downs in a thread
                comment_list = self.get_Debate_Meta_Data(list(collection_debate.find()))

                main_array.append({'title': string_content[0]['title'], 'commentNumber': len(collection) - 1,
                                   'commentInfo': comment_list, 'initTimeStamp': string_content[0]['created_utc'],
                                   'debate_id': str(collection)})

        # Sort the data within the main_array
        main_array_sorted = sorted(main_array, key=lambda k: k['initTimeStamp'], reverse=False)

        data["data"] = main_array_sorted
        return simplejson.dumps(data)

    def get_Debate_Meta_Data(self, comments_cursor):

        dict_to_be_returned = {
            'ups': 0,
            'downs': 0
        }

        # Iterates over every comment
        for i, val in enumerate(comments_cursor):

            if i == 0:
                continue

            if val.get("con_text") == '' or val.get("con_text") is None:
                dict_to_be_returned['ups'] += 1

            else:
                dict_to_be_returned['downs'] += 1

        return dict_to_be_returned


    def is_Not_Used(self):
        pass