# Twitter Sentiment Portfolio Trading

![GitHub](https://img.shields.io/github/license/iampratyush4/Twitter_Sentiment_Portfolio_Trading)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

A data-driven algorithmic trading strategy that leverages Twitter sentiment analysis to construct and rebalance a stock portfolio. This project aims to outperform traditional market benchmarks by prioritizing stocks with strong positive social media engagement.

## 📌 Project Overview

This repository implements a systematic approach to portfolio management using sentiment analysis on Twitter data. By analyzing aggregated sentiment scores for stocks, the strategy selects top-performing equities monthly and rebalances the portfolio to align with current market sentiment trends. The performance is benchmarked against NASDAQ/QQQ to evaluate effectiveness:cite[1]:cite[4].

Key components include:
- **Sentiment Data Aggregation**: Monthly sentiment calculation for stocks using NLP techniques:cite[5]:cite[7].
- **Stock Selection**: Cross-sectional ranking to identify top stocks based on sentiment:cite[1]:cite[4].
- **Portfolio Rebalancing**: Monthly updates to maintain alignment with sentiment trends:cite[1]:cite[3].
- **Performance Benchmarking**: Comparison with NASDAQ/QQQ returns:cite[1]:cite[4].

## 🛠 Features

- **Twitter Data Integration**: Fetches and processes tweets related to target stocks using Twitter API:cite[9].
- **Sentiment Analysis Pipeline**:
  - Text preprocessing (stopword removal, lemmatization, etc.):cite[7].
  - Sentiment scoring using NLP models (e.g., Logistic Regression, SVM):cite[7]:cite[5].
- **Portfolio Construction**:
  - Monthly aggregation of sentiment scores:cite[1].
  - Selection of top 5 stocks using cross-sectional ranking:cite[4].
- **Performance Tracking**:
  - Calculation of portfolio returns with monthly rebalancing:cite[1].
  - Comparative analysis against NASDAQ/QQQ:cite[4].

## ⚙️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/iampratyush4/Twitter_Sentiment_Portfolio_Trading.git
   cd Twitter_Sentiment_Portfolio_Trading
