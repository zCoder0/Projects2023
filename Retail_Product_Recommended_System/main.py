from src.exception.ExceptionBase import ProjectException
import sys
import os
import pickle as pk
import pandas as pd
class Recommended:
    
    def read_dataset(self,path):
        try:
            data_set = pd.read_csv(path)
            return data_set
        except Exception as e:
            ProjectException(e,sys)
    
    def load_model(self,path):
        try:
            with open(path, 'rb') as file:
                model = pk.load(file)
            
            return model
        except Exception as e:
            ProjectException(e,sys)
            
    def __init__(self):
        try:
            path="src\\components\\model\\model.pkl"
            dataset_path = "src\\components\\dataset\\clean_dataset.csv"
            df_path = "src\\components\\dataset\\clean_df.csv"
            
            self.model = self.load_model(path)
            self.dataset = self.read_dataset(dataset_path)
            self.df = self.read_dataset(df_path)
            
        except Exception as e:
            ProjectException(e,sys)
            
    def collaborativeFilering(self,customer_id):
        try:
            all_products = self.df['StockCode'].unique()

            print(all_products)
            # Predict ratings for all products
            predictions = [self.model.predict(customer_id, product) for product in all_products]


            print(predictions)
            # Sort recommendations
            top_recommendations = sorted(predictions, key=lambda x: x.est, reverse=True)[:10]

            # Create a mapping of StockCode to Description
            product_mapping = self.df[['StockCode', 'Description']].drop_duplicates()

            # Convert to dictionary for quick lookup
            product_dict = dict(zip(product_mapping['StockCode'], product_mapping['Description']))

            # Display recommended product names
            print("Top Recommended Products for Customer:", customer_id)
            for rec in top_recommendations:
                product_id = rec.iid  # Extract Product ID
                product_name = product_dict.get(product_id, "Unknown Product")  # Get name from dictionary
                print(f"Product: {product_name} (ID: {product_id}), Estimated Rating: {rec.est:.2f}")
                
        except Exception as e:
            ProjectException(e,sys)


if __name__ == "__main__":
    model = Recommended()
    c_id = input("enter the customer id ")
    model.collaborativeFilering(c_id)
