import os
import google.generativeai as genai
import textwrap
from langchain import PromptTemplate ,LLMChain
from content import API_KEY

from IPython.display import Markdown

class FlashModel:

    def __init__(self):
        os.environ["GOOGLE_API_KEY"]=API_KEY
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return None

        
    def predict(self , query):
        template = f"""
              User Query: {query}
              Task : Generate a helpful, clear, and accurate response based on the user's query and the provided context
              Guidelines:
                      - Use concise language but provide enough detail to fully address the query.
                      - If technical, include examples or explanations where necessary.
                      - Be friendly and professional in tone.
                      - Do not include unverifiable or speculative information.
                      - If additional clarification is needed, ask the user directly.
              Response: 
        """
        template1 =f"""
        User Query ;{query}
        Guidlines : explain simply in 10 words
        """
        
        res =  self.generate_response(template)
        if res:
            return res
        else:
            return ":| Flash A"
     
    def predict1(self,text):
        responce = self.model.generate_content(text)
        res = responce.text
        
        return res
    
