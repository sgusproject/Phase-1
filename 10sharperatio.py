# Sharpe Ratios of Stocks using yfinance
# Libraries: pandas, matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

timeperiod=365

df = yf.Ticker("BA").history(start="2015-01-01", end="2021-07-20", interval="1d").reset_index()[["Date","Open"]]

df = df.rename(columns = {"Open":"ba"})
df["Date"] = pd.to_datetime(df["Date"])

gedata = yf.Ticker("GE").history(start="2015-01-01", end="2021-07-20", interval="1d").reset_index()[["Date","Open"]]
gedata = gedata.rename(columns = {"Open":"ge"})
gedata["Date"] = pd.to_datetime(gedata["Date"])

df = df.merge(gedata, on="Date", how="left")

df["baret"] = 100 *(df["ba"]/df["ba"].shift(timeperiod) -1)
df["geret"] = 100 *(df["ge"]/df["ge"].shift(timeperiod) -1)

df["bastd"] = df["baret"].rolling(timeperiod).std()
df["gestd"] = df["geret"].rolling(timeperiod).std()

df["basharpe"] = df["baret"]/df["bastd"]
df["gesharpe"] = df["geret"]/df["gestd"]

plt.style.use("dark_background")

plt.plot(df["Date"],df["basharpe"], label="BA")
plt.plot(df["Date"],df["gesharpe"], label="GE")
#plt.plot(df["Date"],df["gesharpe"] - df["basharpe"], label="XMR - BTC")
plt.title("Sharpe Ratios of BA and GE", size = 20)
plt.legend()
plt.show()
