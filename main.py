# Import necessary libraries
import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import pandas as pd
import plotly.express as px
import datetime
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
from keys import client_id, client_secret, user_agent

# Download VADER lexicon
nltk.download('vader_lexicon')

# reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)
# VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# Define the subreddit, keywords, and minimum upvote threshold
# this is scraping the data from https://www.reddit.com/r/gaming/
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
hist = px.histogram(df, x='sentiment', title='Distribution of Sentiment Scores for Reddit Posts')
hist.show()

# Time Series Plot
# Filter posts from the last 5 years
current_time = datetime.datetime.now()
five_years_ago = current_time - datetime.timedelta(days=5 * 365)

# Ensure the 'created_utc' column is datetime
df_last_5_years = df[df['created_utc'] >= five_years_ago]

# Group by keyword and resample by month
df_last_5_years['month'] = df_last_5_years['created_utc'].dt.to_period('M').astype(str)  # Convert Period to string
keyword_monthly_counts = df_last_5_years.groupby(['month', 'keyword']).size().unstack(fill_value=0)

# Select top 10 keywords
top_keywords = df['keyword'].value_counts().head(10).index
keyword_monthly_counts_top10 = keyword_monthly_counts[top_keywords]

# Plot time series
fig = px.line(
    keyword_monthly_counts_top10,
    title="Keyword Mentions Over Time (Last 5 Years)",
    labels={"value": "Count", "month": "Time"},
)
fig.show()

# Word Cloud
# Create a dictionary of keyword frequencies
keyword_freq = df['keyword'].value_counts().to_dict()

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(keyword_freq)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Keyword Word Cloud", fontsize=16)
plt.show()

# Heat-Map
# Categorize sentiments into positive, neutral, and negative
df['sentiment_category'] = pd.cut(
    df['sentiment'],
    bins=[-1, -0.05, 0.05, 1],
    labels=['Negative', 'Neutral', 'Positive']
)

# Create a pivot table with keywords as rows and sentiment categories as columns
heatmap_data = df.pivot_table(
    index='keyword',
    columns='sentiment_category',
    values='post_text',
    aggfunc='count',
    fill_value=0
)

# Select top 10 keywords
heatmap_data_top10 = heatmap_data.loc[top_keywords]

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(
    heatmap_data_top10,
    annot=True,
    fmt="d",
    cmap="coolwarm",
    cbar=True,
)
plt.title("Sentiment Heatmap by Keyword", fontsize=16)
plt.ylabel("Keyword", fontsize=12)
plt.xlabel("Sentiment Category", fontsize=12)
plt.show()
