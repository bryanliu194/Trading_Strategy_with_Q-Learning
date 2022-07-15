import datetime as dt
import pandas as pd
from util import get_data
import matplotlib.pyplot as plt


def author():
    return 'bliu386'


def indicator_plot(symbol="JPM", window=14, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31)):
    # initial JPM price[0]---------------------------------
    days0 = pd.date_range(start=sd, end=sd + dt.timedelta(days=14))
    df0 = get_data([symbol], days0, addSPY=False)
    df0.dropna(inplace=True)
    price0 = df0.iloc[0][0]

    # get JPM prices from (sd-window) to ed -----------------------------------
    days = pd.date_range(start=sd - dt.timedelta(days=window + 14), end=ed)
    df = get_data([symbol], days, addSPY=False)
    df.dropna(inplace=True)
    df[symbol] = df[symbol] / price0

    # momentum-----------------------------------------
    df['momentum'] = 0.0

    for i in range(df.shape[0]):
        if i - window >= 0:
            df.iat[i, 1] = df.iloc[i][0]/df.iloc[i-window][0] - 1

    # moving average-----------------------------------------
    df['SMA'] = df[symbol].rolling(window=window).mean()

    # Relative Strength Index----------------------------------------
    df['Daily-return'] = df[symbol].diff()
    df['RSI'] = 1.0
    for i in range(df.shape[0]):
        if i >= window:
            gain, loss = 0, 0
            for j in range(window):
                if df.iloc[i-j][3] > 0:

                    gain += df.iloc[i-j][3]
                else:
                    loss -= df.iloc[i-j][3]
            if loss != 0:
                df.iat[i, 4] = 1.0 - 1.0/(1.0 + gain/loss)

    # bollinger band percentage-------------------------------------
    std = df[symbol].std()
    df['upper'] = df['SMA'] + 2 * std
    df['lower'] = df['SMA'] - 2 * std
    df['BBP'] = (df[symbol] - df['lower'])/(df['upper'] - df['lower'])

    # Williams R ------------------------------------
    # df['R'] = 0.0
    # for i in range(df.shape[0]):
    #     low, high = 100, -100
    #     for j in range(1, window):
    #         if df.iloc[i-j][0] > high:
    #             high = df.iloc[i-j][0]
    #         if df.iloc[i-j][0] < low:
    #             low = df.iloc[i-j][0]
    #     df.iat[i, 8] = (high - df.iloc[i][0])/(high - low)

    # Ulcer Index -----------------------------------
    # df['Ulcer'] = 0.0
    # for i in range(df.shape[0]):
    #     high = -100
    #     for j in range(window):
    #         if df.iloc[i - j][0] > high:
    #             high = df.iloc[i - j][0]
    #
    #     summ = 0.0
    #     for j in range(window):
    #         summ += ((df.iloc[i][0] - high) / high)**2
    #
    #     ulcer = (summ/window)**0.5
    #     df.iat[i, 9] = ulcer

    df[symbol+'0'] = df[symbol] * price0

    df = df[df.index >= sd]
    # print(df.head(10))

    # plt.figure()
    # df[symbol].plot()
    # df['SMA'].plot()
    # plt.title('Simple Moving Average of ' + symbol)
    # plt.legend([symbol, 'SMA'])
    # plt.xlabel('Date')
    # plt.ylabel('Normalized price')
    # plt.savefig('SMA.png')

    # plt.figure()
    # df['momentum'].plot()
    # plt.title('Momentum of ' + symbol)
    # plt.xlabel('Date')
    # plt.ylabel('Momentum')
    # plt.savefig('Momentum.png')

    # plt.figure()
    # df['RSI'].plot()
    # plt.axhline(y=0.3, linestyle='dashed', color='orange')
    # plt.axhline(y=0.7, linestyle='dashed', color='orange')
    # plt.title('Relative Strength Index of ' + symbol)
    # plt.xlabel('Date')
    # plt.ylabel('Relative Strength Index')
    # plt.savefig('RSI.png')

    # fig, ax = plt.subplots(2)
    # ax[0].plot(df.index, df[symbol], df.index, df['SMA'], df.index, df['upper'], df.index, df['lower'])
    # ax[1].plot(df.index, df['BBP'])
    # fig.suptitle('Bollinger Band Percentage of ' + symbol)
    # ax[0].legend([symbol, 'SMA', 'upper band', 'lower band'])
    # ax[0].label_outer()
    # ax[0].set(ylabel='Normalized price')
    # ax[1].set(xlabel='Date', ylabel='BBP')
    # ax[1].legend(['BBP'])
    # fig.savefig('BBP.png')

    # plt.figure()
    # df['R'].plot()
    # plt.axhline(y=0.2, linestyle='dashed', color='orange')
    # plt.axhline(y=0.8, linestyle='dashed', color='orange')
    # plt.title('Williams %R of ' + symbol)
    # plt.xlabel('Date')
    # plt.ylabel('Williams %R')
    # plt.savefig('R.png')

    # plt.figure()
    # df['Ulcer'].plot()
    # plt.axhline(y=0.3, linestyle='dashed', color='orange')
    # plt.title('Ulcer Index of ' + symbol)
    # plt.xlabel('Date')
    # plt.ylabel('Ulcer Index')
    # plt.savefig('Ulcer.png')

    return df

