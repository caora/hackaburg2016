from pymongo import MongoClient
import simplejson

# __init__() method is not necessary for use - therefore we ignore that warning here
class Comments:

    def main_Method(self, debateName):

        self.is_Not_Used()

        try:
            # Connect to database
            connection = MongoClient('mongodb://ds013290.mlab.com', 13290)
            db = connection["heroku_lzs554jn"]
            db.authenticate('admin', 'admin')

            # The data object which will be morphed into a json later on
            data = {}
            mainArray = []

            collection = db.get_collection(debateName).find()

            mainArray.append({'author': collection[0]['author'],
                              'selfText': collection[0]['self_text'],
                              'proText': collection[0]['pro_text'],
                              'conText': collection[0]['con_text'],
                              'title': collection[0]['title'],
                              'timestamp': collection[0]['created_utc'],
                              'commentID': collection[0]['comment_id']})

            # Iterates over every collection
            for i, entry in enumerate(collection):

                if i == 0:
                    continue

                status = ""
                commentText = ""

                if entry['pro_text'] == '':
                    status = "con"
                    commentText = entry['con_text']

                else:
                    status = "pro"
                    commentText = entry['pro_text']

                # Adds a comment to the list which will be given
                mainArray.append({'author': entry['author'],
                                  'commentText': commentText,
                                  'status': status,
                                  'title': entry['title'],
                                  'commentID': entry['comment_id'],
                                  'timestamp': entry['created_utc']})

            # Sorts the comments within the json array
            mainArray_sorted = sorted(mainArray, key=lambda k: k['timestamp'], reverse=False)

            data["data"] = mainArray_sorted

            # Jsonifies the data we want to return
            return simplejson.dumps(data)

        except:
            return "FAIL"

    def is_Not_Used(self):
        pass