import pandas
from src.exception.exception_base import ProjectException
from src.components.data_integtion import DataCollection
from src.components.data_preprocessing import Preprocessing
from src.components.model import Model
import sys
import asyncio
try:
    print("This is main ")


    collector = DataCollection()
    # Run the login and data collection methods asynchronously.
    async def main():
        await collector.login(
            auth_info_1="",
            auth_info_2="",
            password=""
        )
        await collector.get_data("Tamil Movies")
    
    asyncio.run(main())
    tweets = collector.get()
    
    dp = Preprocessing()
    df = dp.preprocessing(tweets)
    
    model =Model()
    df[['finebert_score', 'finebert_sentiment']] = df.apply(model.get_finebert_sentiment, axis=1)
    print("FineBERT sentiment analysis done ")
    
except Exception as e:
    ProjectException(e,sys)