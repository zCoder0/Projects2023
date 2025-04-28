# Stock Price Prediction using ARIMA

## Overview
This project is a **Stock Price Prediction** tool built using **Streamlit** and **ARIMA (AutoRegressive Integrated Moving Average)** model. It allows users to input a stock ticker symbol (e.g., AAPL, TSLA) and predicts the stock price for the next hour based on historical data.

## Features
- **User Input**: Users can enter a stock ticker symbol.
- **Data Retrieval**: Fetches historical stock price data.
- **ARIMA Model Training**: Trains an ARIMA model on stock price data.
- **Price Prediction**: Predicts the next hour's stock price.
- **Visualization**: Displays actual and predicted prices using **Matplotlib**.
- **Interactive UI**: Built with **Streamlit** for a user-friendly experience.

## Installation
### Prerequisites
Ensure you have Python installed. You can install required dependencies using:

```sh
pip install -r requirements.txt
```

### Required Libraries
- **Streamlit** (for UI)
- **Pandas** (for data handling)
- **Matplotlib** (for plotting)
- **ARIMA** (for stock prediction)

## Usage
Run the Streamlit app using the following command:

```sh
streamlit run app.py
```

### Steps to Use:
1. Enter the stock ticker (e.g., AAPL, TSLA).
2. Click the **Predict Next Hour Price** button.
3. View the predicted stock price and graph visualization.

## Project Structure
```
project_root/
│── src/
│   ├── exception/
│   │   ├── exception.py  # Custom exception handling
│   ├── Model/
│   │   ├── model.py  # ARIMA model implementation
│── index.py  # Main Streamlit application
│── README.md  # Project documentation
│── requirements.txt  # Dependencies
```

## Error Handling
- If stock data is unavailable, an error message is displayed.
- Exceptions are logged using a custom `ProjectException` class.

## Future Enhancements
- Support for multi-step predictions (e.g., next 24 hours).
- Integration with **LSTM** for deep learning-based predictions.
- Real-time stock price updates.

## Author
Developed by **Prem Raj**

## License
This project is licensed under the MIT License.

