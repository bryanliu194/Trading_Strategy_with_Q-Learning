import datetime as dt
import pandas as pd
from ManualStrategy import ManualStrategy
from marketsimcode import compute_portvals
import StrategyLearner as sl
import matplotlib.pyplot as plt


class Experiment2:
    def __init__(self, symbol='JPM', sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), osd=dt.datetime(2010, 1, 1), oed=dt.datetime(2011, 12, 31), sv=100000,
                 commission=0.0, impact=0.0):
        self.symbol = symbol
        self.sd = sd
        self.ed = ed
        self.osd = osd  # out of sample start date
        self.oed = oed  # out of sample end date
        self.sv = sv
        self.commission = commission
        self.impact = impact

    def generate_chart(self):
        plt.figure()

        learner0, num0 = self.strategy(0.001)
        learner0 = learner0 / learner0[0]
        learner0.plot()

        learner1, num1 = self.strategy(0.003)
        learner1 = learner1 / learner1[0]
        learner1.plot()

        learner2, num2 = self.strategy(0.005)
        learner2 = learner2 / learner2[0]
        learner2.plot()

        # learner3, num3 = self.strategy(0.008)
        # learner3 = learner3 / learner3[0]
        # learner3.plot()

        # learner4, num4 = self.strategy(0.009)
        # learner4 = learner4 / learner4[0]
        # learner4.plot()

        plt.xlabel('Date')
        plt.ylabel('Normalized Price')
        plt.legend(['Impact 0.001', 'Impact 0.003', 'Impact 0.005'])
        plt.title('Experiment 2 (In-Sample JPM)')
        plt.savefig('experiment2.png')

        impact = [0.001, 0.003, 0.005]
        num = [num0, num1, num2]

        plt.figure()
        plt.plot(impact, num)
        plt.xlabel('Impact')
        plt.ylabel('Total Trades')
        plt.title('Experiment 2 Impact vs. Total Trades')
        plt.savefig('experiment2b.png')

    def strategy(self, impact):
        learner = sl.StrategyLearner(verbose=False, impact=impact, commission=0)
        learner.add_evidence(symbol=self.symbol, sd=self.sd, ed=self.ed, sv=self.sv)
        trades = learner.testPolicy(symbol=self.symbol, sd=self.sd, ed=self.ed, sv=self.sv)
        trades.insert(0, 'Symbol', self.symbol)
        result = compute_portvals(trades, start_val=self.sv, commission=0, impact=impact)
        # print(f'strategy 2 in {result.iloc[-1]}')

        return [result, trades.shape[0]]
