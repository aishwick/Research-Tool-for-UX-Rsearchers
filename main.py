# Import necessary libraries
import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import pandas as pd
import plotly.express as px

# Download VADER lexicon
nltk.download('vader_lexicon')

# reddit instance
reddit = praw.Reddit(
    client_id="fwQ0Fwzbye7tXhTKKM7Tpg",
    client_secret="PLAplE15jwH8Lji4--mbswZWw-eKag",
    user_agent="script:Aish:v1.0 (by /u/Hungry_Gift)"
)
# VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# Define the subreddit, keywords, and minimum upvote threshold
subreddit = reddit.subreddit("gaming")
keywords = ["privacy", "phish", "breach", "2fa", "mfa", "ddos", "vpn", "security", "malicious", "doxx", "ip address exposure", "account theft", "account hacking", "in-game privacy", "phishing scams", "data breach", "ransomware", "malware", "virtual currency scam", "social engineering", "account security", "game client vulnerability", "metadata exposure"]
min_upvotes = 5
posts_data = []

# scrape posts by searching for each keyword
for keyword in keywords:
    for post in subreddit.search(keyword, time_filter="all"):
        # Check if post meets the upvote condition and check if bodytext is not empty
        if post.score > min_upvotes and post.selftext:
            # Run VADER sentiment analysis
            sentiment = analyzer.polarity_scores(post.selftext)

            # Append post data as a dictionary, including the keyword
            post_dict = {
                "game": post.title,
                "post_text": post.selftext,
                "sentiment": sentiment['compound'],
                "keyword": keyword
            }
            posts_data.append(post_dict)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(posts_data)

# Display the total posts and DataFrame
print(f"Total posts stored: {len(df)}")

# Group by 'keyword' and count the number of posts for each keyword
keyword_counts = df['keyword'].value_counts().reset_index()
keyword_counts.columns = ['keyword', 'post_count']  # Rename columns for clarity

# Display the table
print("Number of posts scraped for each keyword:")
print(keyword_counts)

# Count total rows with NaN in 'sentiment'
nan_count = df['sentiment'].isna().sum()
print(f"Total posts with NaN sentiment: {nan_count}")

# Histogram of sentiment scores
hist = px.histogram(df, x='Sentiment Value', title='Distribution of Sentiment Scores for Reddit Posts')
hist.show()

# Additional plot
