from pymongo import MongoClient
import time
import datetime

# __init__() method is not necessary for use - therefore we ignore that warning here
class DebateCloser:

    def main_Method(self):

        self.is_Not_Used()

        mongo_DB_Client_Instance = MongoClient('mongodb://ds013290.mlab.com', 13290)
        mongo_DB_Instance = mongo_DB_Client_Instance["heroku_lzs554jn"]
        mongo_DB_Instance.authenticate('admin', 'admin')

        # Iterate over all collections within the database
        for collection in mongo_DB_Instance.collection_names():

            # If debate is in the collections name and it is not vot
            if 'debate' in collection and 'vote' not in collection:
                mongo_DB_Requested_Thread = mongo_DB_Instance[str(collection)]
                mongo_DB_Requested_Thread_Cursor = list(mongo_DB_Requested_Thread.find())

                # Gets the first comment within that iterated debate
                # The first comment is always the initial comment
                first_comment_time = mongo_DB_Requested_Thread_Cursor[0].get("created_utc")

                # Gets the current time in seconds
                current_time = time.time()

                # Converts the time_Value into float, otherwise it could not be processed any further...
                now_time_value = float(current_time)
                now_time_converted = datetime.datetime.fromtimestamp(now_time_value).strftime('%d-%m-%Y %H:%M:%S')
                now_time_converted_for_subtraction = datetime.datetime.strptime(now_time_converted, '%d-%m-%Y %H:%M:%S')

                # Converts the time_Value into float, otherwise it could not be processed any further...
                first_comment_value = float(first_comment_time)
                first_comment_converted = datetime.datetime.fromtimestamp(first_comment_value).strftime('%d-%m-%Y %H:%M:%S')
                first_comment_converted_for_subtraction = datetime.datetime.strptime(first_comment_converted, '%d-%m-%Y %H:%M:%S')

                # The value of the time difference between the initial starting comment and the current time
                time_difference = (now_time_converted_for_subtraction - first_comment_converted_for_subtraction).total_seconds()

                # 24 hours converted into seconds
                limit_in_seconds = 60 * 60 * 24

                # Whenever the time exceeds
                if time_difference > limit_in_seconds:

                    # Get the id number of that actually, to old, debate
                    number_of_collection = collection[7:]

                    # Renames the debate from debate_id >> closed_id
                    mongo_DB_Instance[str(collection)].rename('closed_' + str(number_of_collection))

    def is_Not_Used(self):
        pass
