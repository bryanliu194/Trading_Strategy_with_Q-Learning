""""""  		  	   		   	 		  		  		    	 		 		   		 		  
"""  		  	   		   	 		  		  		    	 		 		   		 		  
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		   	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		   	 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		   	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		   	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		   	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		   	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		   	 		  		  		    	 		 		   		 		  
or edited.  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		   	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		   	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		   	 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		   	 		  		  		    	 		 		   		 		  
GT User ID: bliu386 (replace with your User ID)  		  	   		   	 		  		  		    	 		 		   		 		  
GT ID: 903736969 (replace with your GT ID)  		  	   		   	 		  		  		    	 		 		   		 		  
"""  		  	   		   	 		  		  		    	 		 		   		 		  

import datetime as dt
import random  		  	   		   	 		  		  		    	 		 		   		 		  
import pandas as pd
import util as ut
import QLearner as ql
from indicators import indicator_plot


def author():
    return 'bliu386'


class StrategyLearner(object):
    """  		  	   		   	 		  		  		    	 		 		   		 		  
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		   	 		  		  		    	 		 		   		 		  

    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		   	 		  		  		    	 		 		   		 		  
        If verbose = False your code should not generate ANY output.  		  	   		   	 		  		  		    	 		 		   		 		  
    :type verbose: bool  		  	   		   	 		  		  		    	 		 		   		 		  
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		   	 		  		  		    	 		 		   		 		  
    :type impact: float  		  	   		   	 		  		  		    	 		 		   		 		  
    :param commission: The commission amount charged, defaults to 0.0  		  	   		   	 		  		  		    	 		 		   		 		  
    :type commission: float  		  	   		   	 		  		  		    	 		 		   		 		  
    """  		  	   		   	 		  		  		    	 		 		   		 		  
    # constructor  		  	   		   	 		  		  		    	 		 		   		 		  
    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		   	 		  		  		    	 		 		   		 		  
        """  		  	   		   	 		  		  		    	 		 		   		 		  
        Constructor method  		  	   		   	 		  		  		    	 		 		   		 		  
        """  		  	   		   	 		  		  		    	 		 		   		 		  
        self.verbose = verbose  		  	   		   	 		  		  		    	 		 		   		 		  
        self.impact = impact  		  	   		   	 		  		  		    	 		 		   		 		  
        self.commission = commission
        self.learner = None

    def author(self):
        return 'bliu386'

    # this method should create a QLearner, and train it for trading
    def add_evidence(  		  	   		   	 		  		  		    	 		 		   		 		  
        self,  		  	   		   	 		  		  		    	 		 		   		 		  
        symbol="JPM",
        sd=dt.datetime(2008, 1, 1),  		  	   		   	 		  		  		    	 		 		   		 		  
        ed=dt.datetime(2009, 12, 31),
        sv=10000,  		  	   		   	 		  		  		    	 		 		   		 		  
    ):  		  	   		   	 		  		  		    	 		 		   		 		  
        """  		  	   		   	 		  		  		    	 		 		   		 		  
        Trains your strategy learner over a given time frame.  		  	   		   	 		  		  		    	 		 		   		 		  

        :param symbol: The stock symbol to train on  		  	   		   	 		  		  		    	 		 		   		 		  
        :type symbol: str  		  	   		   	 		  		  		    	 		 		   		 		  
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		   	 		  		  		    	 		 		   		 		  
        :type sd: datetime  		  	   		   	 		  		  		    	 		 		   		 		  
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		   	 		  		  		    	 		 		   		 		  
        :type ed: datetime  		  	   		   	 		  		  		    	 		 		   		 		  
        :param sv: The starting value of the portfolio  		  	   		   	 		  		  		    	 		 		   		 		  
        :type sv: int  		  	   		   	 		  		  		    	 		 		   		 		  
        """  		  	   		   	 		  		  		    	 		 		   		 		  

        # add your code to do learning here
        df_indicators = indicator_plot(symbol=symbol, window=14, sd=sd, ed=ed)
        df_mom = pd.qcut(df_indicators['momentum'], 10, labels=range(10))
        df_rsi = pd.qcut(df_indicators['RSI'], 10, labels=range(10))
        df_bbp = pd.qcut(df_indicators['BBP'], 10, labels=range(10))
        # df_r = pd.qcut(df_indicators['R'], 100, labels=range(100))
        # df_sma = pd.qcut(df_indicators['SMA'], 100, labels=range(100))

        self.learner = ql.QLearner(num_states=1000, num_actions=3)

        positions = pd.DataFrame({'position': 0}, index=df_indicators.index)
        cycle = 0
        while cycle < 1000:
            cycle += 1
            new_update = 0

            state = df_mom.iloc[0] * 100 + df_rsi.iloc[0] * 10 + df_bbp.iloc[0]
            action = self.learner.querysetstate(state)

            for i in range(1, df_indicators.shape[0]):
                reward = 0
                if action == 0:
                    reward = (df_indicators.iloc[i][symbol+'0'] - df_indicators.iloc[i-1][symbol+'0'] * (1 + self.impact)) * 1000 - self.commission
                elif action == 2:
                    reward = (df_indicators.iloc[i-1][symbol+'0'] * (1 - self.impact) - df_indicators.iloc[i][symbol+'0']) * 1000 - self.commission

                state = df_mom.iloc[i] * 100 + df_rsi.iloc[i] * 10 + df_bbp.iloc[i]
                action = self.learner.query(state, reward)

                if positions.iloc[i]['position'] != action:
                    positions.iat[i, 0] = action
                    new_update += 1

            if new_update < 1:
                if self.verbose:
                    print('converged')
                break

        # example usage of the old backward compatible util function
        # syms = [symbol]
        # dates = pd.date_range(sd, ed)
        # prices_all = ut.get_data(syms, dates)  # automatically adds SPY
        # prices = prices_all[syms]  # only portfolio symbols
        # prices_SPY = prices_all["SPY"]  # only SPY, for comparison later
        # if self.verbose:
        #     print(prices)
        #
        # # example use with new colname
        # volume_all = ut.get_data(
        #     syms, dates, colname="Volume"
        # )  # automatically adds SPY
        # volume = volume_all[syms]  # only portfolio symbols
        # volume_SPY = volume_all["SPY"]  # only SPY, for comparison later
        # if self.verbose:
        #     print(volume)

    # this method should use the existing policy and test it against new data
    def testPolicy(  		  	   		   	 		  		  		    	 		 		   		 		  
        self,  		  	   		   	 		  		  		    	 		 		   		 		  
        symbol="JPM",
        sd=dt.datetime(2010, 1, 1),
        ed=dt.datetime(2011, 12, 31),
        sv=10000,  		  	   		   	 		  		  		    	 		 		   		 		  
    ):  		  	   		   	 		  		  		    	 		 		   		 		  
        """  		  	   		   	 		  		  		    	 		 		   		 		  
        Tests your learner using data outside of the training data  		  	   		   	 		  		  		    	 		 		   		 		  

        :param symbol: The stock symbol that you trained on on  		  	   		   	 		  		  		    	 		 		   		 		  
        :type symbol: str  		  	   		   	 		  		  		    	 		 		   		 		  
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		   	 		  		  		    	 		 		   		 		  
        :type sd: datetime  		  	   		   	 		  		  		    	 		 		   		 		  
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		   	 		  		  		    	 		 		   		 		  
        :type ed: datetime  		  	   		   	 		  		  		    	 		 		   		 		  
        :param sv: The starting value of the portfolio  		  	   		   	 		  		  		    	 		 		   		 		  
        :type sv: int  		  	   		   	 		  		  		    	 		 		   		 		  
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		   	 		  		  		    	 		 		   		 		  
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		   	 		  		  		    	 		 		   		 		  
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		   	 		  		  		    	 		 		   		 		  
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		   	 		  		  		    	 		 		   		 		  
        :rtype: pandas.DataFrame  		  	   		   	 		  		  		    	 		 		   		 		  
        """  		  	   		   	 		  		  		    	 		 		   		 		  

        # # here we build a fake set of trades
        # # your code should return the same sort of data
        # dates = pd.date_range(sd, ed)
        # prices_all = ut.get_data([symbol], dates)  # automatically adds SPY
        # trades = prices_all[[symbol,]]  # only portfolio symbols
        # trades_SPY = prices_all["SPY"]  # only SPY, for comparison later
        # trades.values[:, :] = 0  # set them all to nothing
        # trades.values[0, :] = 1000  # add a BUY at the start
        # trades.values[40, :] = -1000  # add a SELL
        # trades.values[41, :] = 1000  # add a BUY
        # trades.values[60, :] = -2000  # go short from long
        # trades.values[61, :] = 2000  # go long from short
        # trades.values[-1, :] = -1000  # exit on the last day
        # if self.verbose:
        #     print(type(trades))  # it better be a DataFrame!
        # if self.verbose:
        #     print(trades)
        # if self.verbose:
        #     print(prices_all)
        df_indicators_test = indicator_plot(symbol=symbol, window=14, sd=sd, ed=ed)
        df_mom = pd.qcut(df_indicators_test['momentum'], 10, labels=range(10))
        df_rsi = pd.qcut(df_indicators_test['RSI'], 10, labels=range(10))
        df_bbp = pd.qcut(df_indicators_test['BBP'], 10, labels=range(10))
        # df_r = pd.qcut(df_indicators_test['R'], 100, labels=range(100))
        # df_sma = pd.qcut(df_indicators_test['SMA'], 100, labels=range(100))

        trades = pd.DataFrame({'Order': 0}, index=df_indicators_test.index)
        position = 0
        for date, _ in trades.iterrows():
            # date = trades.index[i]
            # if date in df_indicators_test.index:
            state = df_mom[date] * 100 + df_rsi[date] * 10 + df_bbp[date]
            action = self.learner.querytable(state)
            order = 0
            if action == 0:
                if position == 0:
                    order = 1000
                elif position == -1000:
                    order = 2000
                position = 1000
            elif action == 1:
                if position == -1000:
                    order = 1000
                elif position == 1000:
                    order = -1000
                position = 0
            elif action == 2:
                if position == 1000:
                    order = -2000
                elif position == 0:
                    order = -1000
                position = -1000

            if order == 0:
                trades.drop(date, inplace=True)
            else:
                trades.loc[date] = order
                # trades.iat[i, 1] = position

        return trades  		  	   		   	 		  		  		    	 		 		   		 		  


if __name__ == "__main__":
    print("One does not simply think up a strategy")  		  	   		   	 		  		  		    	 		 		   		 		  
