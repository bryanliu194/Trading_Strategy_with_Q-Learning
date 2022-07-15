import datetime as dt
import pandas as pd
from ManualStrategy import ManualStrategy
from marketsimcode import compute_portvals
import StrategyLearner as sl
import matplotlib.pyplot as plt


class Experiment1:
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
        benchmark_out = self.benchmark(self.osd, self.oed)
        manual_out, manual_trades_out = self.manual(self.osd, self.oed)
        benchmark = self.benchmark(self.sd, self.ed)
        manual, manual_trades = self.manual(self.sd, self.ed)
        strategy_learner = self.strategy()

        # cr_manual_in = (manual[-1] / manual[0]) - 1.0
        # cr_bench_in = (benchmark[-1] / benchmark[0]) - 1.0
        # cr_manual_out = (manual_out[-1] / manual_out[0]) - 1.0
        # cr_bench_out = (benchmark_out[-1] / benchmark_out[0]) - 1.0

        benchmark_out = benchmark_out / benchmark[0]
        manual_out = manual_out / manual[0]
        benchmark = benchmark/benchmark[0]
        manual = manual / manual[0]
        strategy_learner = strategy_learner / strategy_learner[0]

        # print('in-sample')
        # std_manual_in = manual.std()
        # std_bench_in = benchmark.std()
        # mean_manual_in = manual.mean()
        # mean_bench_in = benchmark.mean()
        # print(cr_manual_in)
        # print(cr_bench_in)
        # print(std_manual_in)
        # print(std_bench_in)
        # print(mean_manual_in)
        # print(mean_bench_in)

        # print('out-sample')
        # std_manual_out = manual_out.std()
        # std_bench_out = benchmark_out.std()
        # mean_manual_out = manual_out.mean()
        # mean_bench_out = benchmark_out.mean()
        # print(cr_manual_out)
        # print(cr_bench_out)
        # print(std_manual_out)
        # print(std_bench_out)
        # print(mean_manual_out)
        # print(mean_bench_out)

        plt.figure()
        benchmark.plot(style='g')
        manual.plot(style='r')
        strategy_learner.plot()
        plt.xlabel('Date')
        plt.ylabel('Normalized Price')
        plt.legend(['Benchmark', 'Manual Strategy', 'Strategy Q-Learner'])
        plt.title('Experiment 1 (In-Sample JPM)')
        plt.savefig('experiment1.png')

        plt.figure()
        benchmark_out.plot(style='g')
        manual_out.plot(style='r')

        position = 0
        for date, row in manual_trades_out.iterrows():
            position += row[-1]
            if row[-1] > 0 and position > 0:
                plt.axvline(x=date, color='blue', linewidth=.5)
            elif row[-1] < 0 and position < 0:
                plt.axvline(x=date, color='black', linewidth=.5)

        plt.xlabel('Date')
        plt.ylabel('Normalized Price')
        plt.legend(['Benchmark', 'Manual Strategy'])
        plt.title('Manual Strategy vs. Benchmark (Out-of-Sample)')
        plt.savefig('manual1.png')

        plt.figure()
        benchmark.plot(style='g')
        manual.plot(style='r')

        position = 0
        for date, row in manual_trades.iterrows():
            position += row[-1]
            if row[-1] > 0 and position > 0:
                plt.axvline(x=date, color='blue', linewidth=.5)
            elif row[-1] < 0 and position < 0:
                plt.axvline(x=date, color='black', linewidth=.5)

        plt.xlabel('Date')
        plt.ylabel('Normalized Price')
        plt.legend(['Benchmark', 'Manual Strategy'])
        plt.title('Manual Strategy vs. Benchmark (In-Sample)')
        plt.savefig('manual2.png')

    def benchmark(self, sd, ed):
        trades_bench = pd.DataFrame({'Symbol': self.symbol, 'Order': 0}, index=pd.date_range(start=sd, end=ed))
        trades_bench.loc[sd] = [self.symbol, 1000]
        # print(trades_bench)
        result = compute_portvals(trades_bench, start_val=self.sv, commission=self.commission, impact=self.impact)
        # print(f'benchmark {result.iloc[-1]}')
        return result

    def manual(self, sd, ed):
        ms = ManualStrategy()
        trades = ms.testPolicy(symbol=self.symbol, sd=sd, ed=ed, sv=self.sv)
        result = compute_portvals(trades, start_val=self.sv, commission=self.commission, impact=self.impact)

        # print(f'manual {result.iloc[-1]}')
        return result, trades

    def strategy(self):
        learner = sl.StrategyLearner(verbose=False, impact=self.impact, commission=self.commission)
        learner.add_evidence(symbol=self.symbol, sd=self.sd, ed=self.ed, sv=self.sv)
        trades = learner.testPolicy(symbol=self.symbol, sd=self.sd, ed=self.ed, sv=self.sv)
        trades.insert(0, 'Symbol', self.symbol)
        result = compute_portvals(trades, start_val=self.sv, commission=self.commission, impact=self.impact)
        # print(f'strategy in {result.iloc[-1]}')

        # trades2 = learner.testPolicy(symbol=self.symbol, sd=self.osd, ed=self.oed, sv=self.sv)
        # print(trades2.head(10))
        # trades2.insert(0, 'Symbol', self.symbol)
        # result2 = compute_portvals(trades2, start_val=self.sv, commission=self.commission, impact=self.impact)
        # print(f'strategy out {result2.iloc[-1]}')

        return result
