import praw
from textblob import TextBlob
import math


reddit = praw.Reddit(client_id='eTntalfT8B5DaQ',
                     client_secret='ggHZrNuVc2sUPXDZdcOXQ7HeNvY',
                     user_agent='detacoll',
                     username='notacoderyet',
                     password='hsn11484')

# opens file with subreddit names
with open('reddit.txt') as f:

    for line in f:
        subreddit = reddit.subreddit(line.strip())

        sub_sentiment = 0
        num_comments = 0

        for submission in subreddit.hot(limit=25):
            if not submission.stickied:
                submission.comments.replace_more(limit=0)
                for comment in submission.comments.list():
                        blob = TextBlob(comment.body)

                        #adds comment sentiment to overall sentiment for subreddit
                        comment_sentiment = blob.sentiment.polarity
                        sub_sentiment += comment_sentiment
                        num_comments += 1

                        print(str(comment.body.encode('utf-8')) + ': ' + str(blob.sentiment.polarity))

        print('/r/' + str(subreddit.display_name))
        try:
            print('Ratio: ' + str(math.floor(sub_sentiment/num_comments*100)) + '\n')
        except:
            print('No comment sentiment.' + '\n')
            ZeroDivisionError
