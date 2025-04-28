import tensorflow as tf
import keras
import pickle
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

data = pd.read_csv("Datasets/Customer_data.csv")

class IntentModel:
  def __init__(self,path="Intent_Model/intent_model.h5"):
    self.model = tf.keras.models.load_model(path)

  def intentLoadEncoder(self,path='Intent_Model/intent_label_encoder.pkl'):
    with open(path, 'rb') as file:
      self.encoder =  pickle.load(file)


  def intentPadded(self,path="Intent_Model/intent_padded.pkl"):
    with open(path, 'rb') as file:
      self.intent_padded = pickle.load(file)

  def intentTokenizer(self,path="Intent_Model/intent_tokenizer.pkl"):
    with open(path, 'rb') as file:
      self.tokenizer = pickle.load(file)

  def get_response(self,user_input):
    self.intentLoadEncoder()
    self.intentPadded()
    self.intentTokenizer()
    sequence = self.tokenizer.texts_to_sequences([user_input])
    padded = pad_sequences(sequence, padding='post', maxlen=self.intent_padded.shape[1])
    predicted_intent = self.model.predict(padded)
    intent_label = self.encoder.inverse_transform([predicted_intent.argmax()])[0]
    response = data[data['intent'] == intent_label]['response'].values[0]
    return response
