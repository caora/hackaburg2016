from flask import Flask, request, redirect, url_for
from threading import Timer
from flask.ext.cors import CORS
from RunningDebates import RunningDebates
from CreateDebate import CreateDebate
from Comments import Comments
from CreateComment import CreateComment
from CommentVote import CommentVote
from OverViewVotes import OverViewVotes
from DebateCloser import DebateCloser
import threading

app = Flask(__name__)
CORS(app)
runDebates = RunningDebates()
createDebates = CreateDebate()
comments = Comments()
createComments = CreateComment()
commentVote = CommentVote()
#overViewVotes = OverViewVotes()
#debateCloser = DebateCloser()

#RUNNING DEBATES
@app.route("/dashboard/runningDebates", methods=['GET'])
def dashboard():
    return runDebates.main_Method()

#CREATE DEBATE
@app.route("/createDebate", methods=['POST'])
def createDebate():
    return createDebates.main_Method(request)

#GET DEBATE COMMENTS
@app.route("/comments/debate/<string:debateName>/", methods=['GET'])
def getComments(debateName):
    return comments.main_Method(debateName)

#CREATE DEBATE COMMENT
@app.route("/createComment", methods=['POST'])
def createComment():
    return createComments.main_Method(request)

#VOTE COMMENT
@app.route("/voteComment", methods=['POST'])
def voteComment():
    return commentVote.main_Method(request)


#def refreshVoteOverview():
    #overViewVotes.main_Method()
    #debateCloser.main_Method()
    # call refreshVoteOverview() again in 60 seconds
    #threading.Timer(60, refreshVoteOverview).start()

#refreshVoteOverview()


if __name__ == "__main__":
    app.run(host="0.0.0.0")