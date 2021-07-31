# Algotrading-Developing algorithms in Quantconnect and Submitting Alpha
## Fintech 5 : Final Project 2nd Aug-14Nov 2021
## Project Report by Lim Chye Joo (t0921038)

## Python IDE: Jupyter (Anaconda)
## Python Codes Best viewed with Jupyter or nbviewer - https://nbviewer.jupyter.org/ .
<p align="center">
## Phase 1: Foundation (2 weeks)
</p>
**OVERVIEW**
To design and develop an intelligent systematic trading system leveraging the fundamentals of
investing and algotrading.

**SKILLS Attained**: 
  - Python Language
  - Google Colab, Jupyter Anaconda, VS Code IDEs. 
  - Python libraries for dataframe manipulation, calculation, ML & Visualization.

)

**A :Fundamentals of Python**

Learning Python, familiarise using Google Colab, Jupyter notebooks and VS Code.
Github was used used for the report writing and storing the codes.
After trying out and familiarizing with how to use Google Colab and Jupyter notebooks, and VS Code. I decided on using Jypyter notebook as it more intuitive and customisable.
Notebook files from Phase1: 01-12 were written to practice using python for:

- Loading data
  - Data resources: Yahoo Finance. 
    - download as .csv files (Colab, Jupyter)
    - downloaded using pandas_data_reader (Jupyter, VSCode)
    - downloaded using yfinance (Jupyter, VSCode)
    - column reading, insert/delete column (Colab, Jupyter)
- Cleaning data
  - normalizing
  - convert string to datetime for computation
- Using Libraries & dependencies: pandas, numpy, matplotlib, sklearn, yfinance, ta, ta.utils.
- Creating Indicators (Technical, Fundamental ) by functions, libraries and Python
- Visualising data using matplotlib

### IDEs used
Initially experimented using Google Colab, Jupyter and VSCode . 
Finally settled with using Jupyter Notebook for most python computation, storing in .ipynb files. 



## Deliverables A: Github Phase-1 Repository

Files 01-12. Codes and files ran and used for calculations of important financial stock indicators:

- [01DataframesLearn.ipynb](https://github.com/sgusproject/Phase-1/blob/main/01DataframesLearn.ipynb)
  - Read data from CSV (downloaded from Yahoo! Finance)
  - Understand dataframe and data types
  - Set Index
  - Parse dates
  - Use Index with loc
  - Use indexing with iloc

- [02DataframesSeries.ipynb](https://github.com/sgusproject/Phase-1/blob/main/02DataframesSeries.ipynb)
  - Use Type to get data type
  - Each column is a Series
  - Series show data type (dtype)
  - Calculate with Series
  - Daily change
  - Daily percentage change
  - Normalize data
  - Similarity with Excel
  - Indexing with Series

- [03DataframeModify.ipynb](https://github.com/sgusproject/Phase-1/blob/main/03DataframeModify.ipynb)
  - Calculate with columns in dataframe
  - Create new columns
  - Drop Columns
  - Min, Max, Argmin, Argmax
  - Mean

- [04DataframeVisualize.ipynb](https://github.com/sgusproject/Phase-1/blob/main/04DataframeVisualize.ipynb)
  - Visualization of data
    -Learning Matplotlib
      -Subplots
      -Multiplots
      -Bar plots
  -Libraries
    - matplotlib
     -pandas

- [05PandasDatareader.ipynb](https://github.com/sgusproject/Phase-1/blob/main/05PandasDatareader.ipynb)
  - Pandas-datareader
    - pip install pandas_datareader to extract data directly from Yahoo Finance
  - Libraries
    - datetime
    - pandas
    - data Yahoo finance, Nasdaq symbols

- [06StockIndicators.ipynb](https://github.com/sgusproject/Phase-1/blob/main/06StockIndicators.ipynb)
  - Calculate Stock Indicators
    - Pct change
    - Log returns
    - Standard Deviation (Volatility)
    - Rolling
    - Simple Moving Average
    - Exponential Moving Average
  - Libraries & Methods
    - pandas
    - numpy
    - matplotlib
    - data from Yahoo Finance csv
    - functions from numpy, pandas

- [07MACD%26Stochastic.ipynb](https://github.com/sgusproject/Phase-1/blob/main/07MACD%26Stochastic.ipynb)
  - MACD & Stochastic Oscillator
    - MACD - Moving average convergence divergence
    - MACD is a lagging indicator when trading on the crossovers
    - https://www.investopedia.com/terms/m/macd.asp
    - Calculation: Will be using default MACD parameters(12-26-9)
    - MACD = 12-Period EMA - 26-Period EMA
    - Signal Line 9-Period EMA

- [08Beta_LR.ipynb](https://github.com/sgusproject/Phase-1/blob/main/08Beta_LR.ipynb)
  - Beta
    Beta is a measure of a stock's volatility to the overall market
    For USA Market: Assumption used, S&P 500 Index has a beta of 1.0
    High-beta stocks are supposed to be riskier but provide higher potential - return
    Low-beta stocks pose less risk but also lower returns.
    Resoures: https://www.investopedia.com/terms/b/beta.asp 

- [09StdDev_pd-Ver2.ipynb](https://github.com/sgusproject/Phase-1/blob/main/09StdDev_pd-Ver2.ipynb)
  - Standard Deviation, Mean, Coefficient Of Variation
  - Generic dataframe for multiple inputs
  - Libraries
    pandas, numpy, matplotlib
    get-dataframe function to get from .csv

- [10SharpeRatios.ipynb](https://github.com/sgusproject/Phase-1/blob/main/10SharpeRatios.ipynb)
  - Sharpe Ratio
  - Using yfinance data downloader
  - %matplotlib notebook for Jupyter interactive chart plotting
  - Libraries
    - yfinance
    - pandas
    - matplotlib
  - Indicators:
    - ave return
    - standard deviation
    - sharpe ratio

- [10sharperatio.py](https://github.com/sgusproject/Phase-1/blob/main/10sharperatio.py)
  - Python code, for learnig to use in VS Code raw python.
    Mirroring results codes above which was rendered in Jupyter Notebook Anaconda.

- [11BollingerBands.ipynb](https://github.com/sgusproject/Phase-1/blob/main/11BollingerBands.ipynb)
  - Bollinger Band®
    A Bollinger Band® is a technical analysis tool defined by a set of trendlines plotted two standard deviations (positively and negatively) away from a simple moving average (SMA) of a security's price, but which can be adjusted to user preferences.

- [12RSI.ipynb](https://github.com/sgusproject/Phase-1/blob/main/12RSI.ipynb)
  - RSI Calculation and plotting


**B: Fundamentals of Quantconnect**
Quantconnect is a very vast tool for developing trading algorithms. First phase is to complete all
the botcamps within quantconnect to get familiar with syntax and functions of QC
- Understanding of Quant Connects Alpha stream
- 
## Deliverable B: Successfully completed all the bootcamps**

![QC Bootcamps Completed](https://github.com/sgusproject/Phase-1/blob/gh-pages/QCBootcamps_Completed.JPG?raw=true)


#### Learning Resources:

- https://www.ta-lib.org/
- https://blog.quantinsti.com/install-ta-lib-python/
- https://www.learnpythonwithrune.org/start-python-with-pandas-for-financial-analysis/
- https://www.programcreek.com/python/example/92312/talib.RSI
- https://www.investopedia.com/

