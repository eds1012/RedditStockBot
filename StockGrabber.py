
import praw
import csv

file = open(r'C:\users\Eric\Desktop\tickers.csv', 'w', newline='')
writer = csv.writer(file)

reddit = praw.Reddit(
    client_id="My_ID",
    client_secret="My_secret",
    password="My_Password",
    user_agent="User_Agent",
    username="My_Username",
)
print(reddit.user.me())
character = set("$")
numbers = ["1","2","3","4","5","6","7","8","9","0"]
titlelist = []
tickers =[]
tocsv=[]
def submission_ticker(sub):
#    titlelist = [title for title in reddit.subreddit(sub).hot(limit=100) if title.title.contains("$")]
    for submission in reddit.subreddit(sub).hot(limit= 10):
        titlelist.append(submission.title)
        for comment in submission.comments:
            print(comment.body)
    for title in titlelist:
        if "$" in title:
            split = title.split(" ")
#        print(split)
            for word in split:
                if "$" in word:
                    for ch in ["!","@","#","%","^","&","*","(",")","?",".",",","/",":",";","...","'"]:
                        if ch in word:
                            word = word.replace(ch,"")
                            word=word.replace("(","")
                            word=word.replace(")","")
                            tickers.append(word)
    for ticker in tickers:
        if not any(word in numbers for word in ticker):
            print(ticker)
            writer.writerow([ticker])
#            tocsv.append(ticker)
#    writer.writerows([tocsv])
submission_ticker("wallstreetbets")
print("Next Subreddit")
#submission_ticker("pennystocks")
file.close()
