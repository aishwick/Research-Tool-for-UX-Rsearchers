Welcome to the *UX Research Analysis Tool*! This guide will help you install, set up, and run the tool from an end-user’s perspective. It is intended for users who want to analyze user discussion data (e.g., from Reddit) to identify common topics, sentiments, and trends. While we use a gaming security example by default, you can apply the same approach to any topic you choose.

**Note**: This is the user’s guide. More detailed technical and architectural details are provided in the developer’s documentation (found in the project’s repository). If you encounter advanced technical issues or wish to modify the code structure, please refer to the developer’s guide.


## Table of Contents

1. [Overview](#overview)  
2. [Requirements](#requirements)  
3. [Installation & Setup](#installation--setup)  
4. [Configuring API Keys](#configuring-api-keys)  
5. [Running the Tool](#running-the-tool)  
6. [Using the Tool - Step-by-Step](#using-the-tool---step-by-step)  
7. [Common Errors & Troubleshooting](#common-errors--troubleshooting)  
8. [Caveats & Limitations](#caveats--limitations)  
9. [Screenshots](#screenshots)



## Overview

The *UX Research Analysis Tool* helps you analyze user discussions (e.g., from Reddit) to uncover sentiment trends, frequently discussed topics, and other insights. Initially, we focus on security concerns in gaming communities, but you can easily adapt the keywords and data sources for other contexts, such as user feedback on apps, product reviews, or forum discussions.

**Key Features**:  
- Scrape data from Reddit or load your own CSV/Excel files of user comments.  
- Analyze sentiment (positive, negative, neutral) using built-in NLP tools.  
- Visualize key insights through bar charts, time-series graphs, word clouds, and heatmaps.  
- Optionally export insights as PDFs (if implemented).

---

## Requirements

- **Python Version**: Python 3.9+ recommended.  
- **Dependencies**: Listed in `requirements.txt`.

You must have Python and `pip` installed. If you’re familiar with Git, you can clone the repository. Otherwise, you can download the project folder as a ZIP and extract it anywhere on your machine.



## Installation & Setup

1. **Clone or Download the Repo**:  
   - Clone via Git:  
     ```bash
     git clone https://github.com/aishwick/Research-Tool-for-UX-Rsearchers.git
     ```
   - Or download as a ZIP from GitHub and unzip it.

2. **Install Dependencies**:  
   Navigate to the project folder in your terminal:
   ```bash
   cd Research-Tool-for-UX-Rsearchers
   pip install -r requirements.txt

Prepare Your Environment (Optional but recommended):
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Configuring API Keys
The tool uses Reddit’s API (via PRAW) for scraping. You need your own Reddit app credentials:
Create a Reddit Account (if you don’t have one):
Go to https://www.reddit.com/ and sign up.
Register an App:
Go to https://www.reddit.com/prefs/apps, click “Create another app...”
Choose script as the app type.
Fill in name and redirect URI (e.g. http://localhost:8080).
Save and note down the client ID and client secret.
keys.py File:
Create a file named keys.py (if it’s not already there) in the project folder:
python
Copy code
# keys.py (example)
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
user_agent = "script:YourAppName:v1.0 (by /u/YourRedditUsername)"
Important: Do not commit keys.py to any public repository. The .gitignore file should already be set to ignore it.
If you don’t intend to scrape Reddit data and prefer to use your own CSV/Excel data, you can skip this step.

Running the Tool
Once keys and dependencies are set:

python main.py

If the project provides a web interface (e.g., via Streamlit), it may prompt instructions like:
Open a browser and go to http://localhost:8501 to interact with the tool via a simple web UI.
If no web UI is implemented yet, data analysis will run and produce output (e.g., charts) directly in the terminal or as image files saved locally.

Using the Tool - Step-by-Step
Prepare Your Data Source:
Scraping from Reddit:
By default, main.py scrapes the r/gaming subreddit for security-related keywords. You can modify the keywords in main.py to suit your research topic.
Using Your Own Data:
Upload a CSV or Excel file containing user comments. The file should have these columns:
Post/Comment: Text of the user’s comment.
User: Username of the poster (optional, but recommended).
Date: Date of the comment (YYYY-MM-DD format recommended).
Topic: A label/classification for the comment (e.g., phishing, account theft).
Place your data file in the project folder or specify the path in main.py.
Run the Analysis:

python main.py
The tool will:
Load or scrape the data.
Clean and process it.
Perform sentiment analysis.
Generate visualizations (e.g., showing frequency of topics, sentiment distribution, etc.).
Interact with Filters (If UI is available): If a web UI is implemented:
Open your browser at http://localhost:8501.
Use sliders or dropdown filters to:
Select sentiment categories (positive, negative, neutral).
Narrow down analysis by specific topics.
Adjust date ranges or other parameters.
View Visualizations: The tool displays:
Bar Charts: Frequency of different security concerns or topics.
Time-Series Plots: How mentions of a certain issue evolve over time.
Word Clouds: Common terms in user discussions.
Heatmaps: Showing sentiment distribution across topics.
Exporting Results: If implemented, click the “Export and Download PDF” button or run the provided command to export the analysis results into a PDF containing key insights, charts, and recommendations.

Common Errors & Troubleshooting
Missing API Keys:
If you see errors about Reddit authentication, check keys.py for correct client_id, client_secret, and user_agent.
Ensure you have valid Reddit credentials and that the app is created as a “script” type in Reddit preferences.
Data Format Issues:
If the tool complains about missing columns, ensure your CSV/Excel file follows the required schema (Post/Comment, User, Date, Topic).
Rate Limits or Scraping Issues:
If Reddit data scraping fails, it might be due to rate limits. Try again later or narrow your keyword search.
Python Version or Dependency Issues:
Make sure you installed dependencies using pip install -r requirements.txt.
If something doesn’t work as expected, confirm you’re using Python 3.9+.

Caveats & Limitations
Current Focus: The example focuses on gaming security. To analyze other topics, you must edit keywords and possibly the data source in main.py.
Limited Reporting Features:
PDF or advanced reporting may not be fully implemented. You might see a placeholder or partial feature.
Performance on Large Datasets:
Very large data sets may slow down analysis. Consider sampling or pre-filtering your data.
Bugs & Incomplete Features:
This tool may have known bugs or unfinished functionalities. For deeper technical details or known issues, please refer to the developer’s documentation.

Screenshots

histogram of sentiment scores
![Model](https://github.com/aishwick/Research-Tool-for-UX-Rsearchers/blob/main/Documentation/Histogram%20showing%20sentiment)

word cloud showing common security terms
![Model](https://github.com/aishwick/Research-Tool-for-UX-Rsearchers/blob/main/word%20cloud%20showing%20common%20security%20terms)

Bar chart showing sentiment
![Model](https://github.com/aishwick/Research-Tool-for-UX-Rsearchers/blob/main/image.png)



