import pickle
import numpy as np
import joblib
import spacy
import nltk
import spacy
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
nltk.download('stopwords')
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))
from IntentModel import IntentModel 

class MyModel:
    nlp= spacy.load('en_core_web_sm')

    def __init__(self):
        
        with open('Models/classification_model.pkl', 'rb') as file:
            self.model = pickle.load(file)

    def loadVector(self):
        with open('Models/tfidf_vectorizer.pkl', 'rb') as file:
            self.vector = pickle.load(file)

    def loadEncoder(self):
        with open('Models/le.pkl', 'rb') as file:
            self.encoder = pickle.load(file)
    def preprocess_text(self,text):
        doc = self.nlp(text.lower())
        tokens = [token.lemma_ for token in doc if token.text not in STOPWORDS and token.is_alpha]
        tokens = [stemmer.stem(token) for token in tokens]
        return ' '.join(tokens)

    def predict(self,text):
        self.loadEncoder()
        self.loadVector()
        text = self.preprocess_text(text)
        text = self.vector.transform([text])
        pred = self.model.predict(text)
        return self.encoder.inverse_transform(pred)[0]
    

