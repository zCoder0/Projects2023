from transformers import BertTokenizer, BertForSequenceClassification
import torch
import pandas as pd
from googletrans import Translator
import emoji

class Model:
    def __init__(self):
        # Load FineBERT model and tokenizer
        self.model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
        self.tokenizer = BertTokenizer.from_pretrained(self.model_name)
        self.model = BertForSequenceClassification.from_pretrained(self.model_name)

        # Initialize translator
        self.translator = Translator()





        # Expanded emoji sentiment dictionary
        self.emoji_sentiment = {
            "😊": 0.2, "👍": 0.2, "😂": 0.15, "🔥": 0.15, "🎉": 0.2, "❤": 0.2, "😍": 0.2, "✨": 0.15, "📈": 0.15,  # Positive
            "😞": -0.2, "👎": -0.2, "😡": -0.15, "💔": -0.15, "😢": -0.2, "😠": -0.15,                     # Negative
            "😐": 0.0, "🤔": 0.0, "🤷": 0.0, "👀": 0.0, "🙄": 0.0                                     # Neutral
        }

        # Dynamic emoji sentiment function
        def get_emoji_boost(self,emojis):
            if not emojis:
                return 0
            boost = 0
            for e in emojis:
                if e in self.emoji_sentiment:
                    boost += self.emoji_sentiment[e]
                else:
                    # Dynamic check using emoji description
                    desc = emoji.demojize(e, delimiters=("", "")).lower()
                    if any(word in desc for word in ["happy", "love", "fire", "up", "heart", "good"]):
                        boost += 0.1  # Positive
                    elif any(word in desc for word in ["sad", "angry", "broken", "down", "bad"]):
                        boost -= 0.1  # Negative
                    else:
                        boost += 0.0  # Neutral
            return boost

    # Sentiment function with emoji boost
    def get_finebert_sentiment(self,row):
        tamil_text = str(row['tamil'])
        english_text = str(row['english'])
        emojis = str(row['emojis'])

        full_text = ""
        if tamil_text !="nan":
            try:
                full_text += self.translator.translate(tamil_text, dest='en').text + " "
            except:
                full_text += ""
        if english_text != "nan":
            full_text += english_text

        if not full_text.strip():
            return pd.Series([0, "Neutral"], index=['score', 'sentiment'])

        # FineBERT prediction
        inputs = self.tokenizer(full_text, return_tensors="pt", truncation=True, padding=True, max_length=128)
        with torch.no_grad():
            outputs = self.model(**inputs)
            scores = outputs.logits.softmax(dim=-1).numpy()[0]

        # Base score
        base_score = scores[2] - scores[0]

        # Emoji boost
        emoji_boost = self.get_emoji_boost(emojis)

        # Final score
        final_score = base_score + emoji_boost

        # Sentiment with threshold
        if final_score > 0.1:
            sentiment = "Positive"
        elif final_score < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return pd.Series([final_score, sentiment], index=['score', 'sentiment'])