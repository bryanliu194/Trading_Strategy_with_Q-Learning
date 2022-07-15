import datetime as dt
import pandas as pd
from indicators import indicator_plot


def author():
    return 'bliu386'


class ManualStrategy:
    def __init__(self):
        pass

    def testPolicy(self, symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=100000):
        df = pd.DataFrame({'Symbol': symbol, 'Order': 0}, index=pd.date_range(start=sd, end=ed))
        # print(df)
        df_indicators = indicator_plot(symbol=symbol, window=14, sd=sd, ed=ed)
        # print(df_indicators.head())

        position = 0
        for i in range(df_indicators.shape[0]):
            signal = 0

            # BBP
            if i > 0:
                bbp0, bbp1 = df_indicators.iloc[i - 1]['BBP'], df_indicators.iloc[i]['BBP']
                if bbp0 < 0 and bbp1 > 0:
                    signal += 1
                elif bbp0 > 1 and bbp1 < 1:
                    signal -= 1

            # RSI
            if df_indicators.iloc[i]['RSI'] > 0.7:
                signal -= 2
            elif df_indicators.iloc[i]['RSI'] > 0.5:
                signal -= 1
            elif df_indicators.iloc[i]['RSI'] > 0.5:
                signal += 1
            elif df_indicators.iloc[i]['RSI'] > 0.3:
                signal += 2

            # momentum
            if df_indicators.iloc[i]['momentum'] > 0.05:
                signal += 1
            elif df_indicators.iloc[i]['momentum'] < 0:
                signal -= 1

            # long
            date = df_indicators.index[i]
            if signal >= 1:
                if position == 0:
                    df.loc[date] = [symbol, 1000]
                    position = 1000
                elif position == -1000:
                    df.loc[date] = [symbol, 2000]
                    position = 1000
            # nothing
            elif signal >= -1:
                if position == -1000:
                    df.loc[date] = [symbol, 1000]
                    position = 0
                elif position == 1000:
                    df.loc[date] = [symbol, -1000]
                    position = 0
            # short
            else:
                if position == 1000:
                    df.loc[date] = [symbol, -2000]
                    position = -1000
                elif position == 0:
                    df.loc[date] = [symbol, -1000]
                    position = -1000

        return df
