import datetime as dt
import pandas as pd
from ManualStrategy import ManualStrategy
from marketsimcode import compute_portvals
from experiment1 import Experiment1
from experiment2 import Experiment2
from util import get_data
import numpy as np
import random

def author():
    return 'bliu386'


class TestProject:
    def __init__(self, symbol='JPM', sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31),
                 osd=dt.datetime(2010, 1, 1), oed=dt.datetime(2011, 12, 31), sv=100000, commission=0.0, impact=0.0):
        self.symbol = symbol
        self.sd = self.get_first_trading_day(sd)
        self.ed = ed
        # self.ed = dt.datetime(2010, 1, 31)
        self.osd = self.get_first_trading_day(osd)  # out of sample start date
        self.oed = oed  # out of sample end date
        self.sv = sv
        self.commission = commission
        self.impact = impact

    def experiment1(self):
        exp = Experiment1(symbol=self.symbol, sd=self.sd, ed=self.ed, osd=self.osd, oed=self.oed, sv=self.sv,
                          commission=self.commission, impact=self.impact)
        exp.generate_chart()

    def experiment2(self):
        exp = Experiment2(symbol=self.symbol, sd=self.sd, ed=self.ed, osd=self.osd, oed=self.oed, sv=self.sv,
                          commission=0, impact=0)
        exp.generate_chart()

    def get_first_trading_day(self, start):
        days = pd.date_range(start=start, end=start + dt.timedelta(days=10))
        price2 = get_data([self.symbol], days, addSPY=False)
        price2 = price2.dropna()
        return price2.index[0]


if __name__ == "__main__":
    random.seed(7)
    test_project = TestProject(
        symbol='JPM',
        sd=dt.datetime(2008, 1, 1),
        ed=dt.datetime(2009, 12, 31),
        osd=dt.datetime(2010, 1, 1),
        oed=dt.datetime(2011, 12, 31),
        sv=100000,
        commission=9.95,
        impact=0.005)

    test_project.experiment1()
    test_project.experiment2()


