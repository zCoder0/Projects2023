
# Sentiment Analysis of Tamil Movies

## Overview
This project performs sentiment analysis on tweets related to "Tamil Movies" using FineBERT, with additional emoji-based sentiment boosting. It collects data from X, processes Tamil and English text, and provides sentiment scores (Positive, Negative, Neutral).

## Features
- Collects tweets from X using `twikit`.
- Splits Tamil and English text with `langdetect`.
- Translates Tamil to English using `google-translator`.
- Analyzes sentiment with FineBERT (`nlptown/bert-base-multilingual-uncased-sentiment`).
- Boosts sentiment scores with emojis (e.g., 🔥📈❤).
- Outputs results in a DataFrame.

## Requirements
- **Python Version**: 3.11.9
- **Dependencies**: pandas
                    streamlit
                    numpy
                    transformers
                    torch
                    textblob
                    emoji
                    langdetect
                    httpx[http2]
                    nest_asyncio
                    twikit
                    httpcore
                    google-translator

## Installation
1. Clone or download the project:
2. Create a virtual environment:
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

3. Install dependencies: (requirements.txt)
pip install -r requirements.txt



## Usage
1. Ensure X credentials are set in `main.py`:
```python

await collector.login(
    auth_info_1="@YourUsername", 
    auth_info_2="your_email@gmail.com", 
    password="your_password")

2.Run the Script

python main.py
Output: Sentiment scores and labels in finebert_score and finebert_sentiment columns.


SentimentAnalysisTamilMovies/
├── src/
│   ├── components/
│   │   ├── data_integtion.py  # Data collection and preprocessing
│   │   └── [other files]
├── main.py                   # Main script
├── tamil_movies_tweets.json  # Tweet data (optional)
├── requirements.txt          # Dependencies
└── README.md                 # This file


text: "Tamil movies semma da 2025 🔥📈❤"
tamil: "semma da"
english: "Tamil movies 2025"
emojis: "🔥📈❤"
finebert_score: 0.55
finebert_sentiment: Positive

## Future Improvements
Add dashboard with Streamlit.
Support real-time tweet streaming.
Expand emoji sentiment dictionary.
Contributing


## Contributing
Feel free to fork, submit PRs, or report issues on GitHub!

## License
MIT License (or your choice).

## Contact
Author: Prem Raj
Email: rajp37590@gmail.com