import datetime as dt
import numpy as np
import pandas as pd
from util import get_data, plot_data


def author():
    return 'bliu386'


def compute_portvals(
        orders_df,
        start_val=100000,
        commission=0.0,
        impact=0.0,
):

    # orders_df = pd.read_csv(orders_file, index_col="Date", parse_dates=True, na_values=["nan"])
    orders_df.sort_index(inplace=True)

    symbols = orders_df["Symbol"].unique()

    days = pd.date_range(start=orders_df.index[0], end=orders_df.index[-1])

    price2 = get_data(symbols, days, addSPY=False)
    price2 = price2.dropna()

    for s in symbols:
        price2[s + '_n'] = 0
    price2['cash'] = 0
    price2['value'] = 0
    price2['cash'] = price2['cash'].astype(float)
    price2['value'] = price2['value'].astype(float)

    for i in range(price2.shape[0]):
        if i != 0:
            for s in symbols:
                c = price2.columns.get_loc(s + "_n")
                price2.iat[i, c] = price2.iloc[i - 1, c]
            price2.iat[i, -2] = price2.iloc[i - 1, -2]
            price2.iat[i, -1] = price2.iloc[i - 1, -1]
        else:
            price2.iat[i, -2] = start_val
            price2.iat[i, -1] = start_val

        day = price2.index[i]

        if day not in orders_df.index:
            total_value = 0
            for s in symbols:
                c = price2.columns.get_loc(s + "_n")
                price2.iat[i, c] = price2.iloc[i - 1, c]
                total_value += price2.iloc[i][s] * price2.iloc[i][s + "_n"]

            price2.iat[i, -2] = price2.iloc[i - 1, -2]
            price2.iat[i, -1] = total_value + price2.iloc[i, -2]
            continue

        find = orders_df.loc[[day]]

        row_num = 0
        for row in find.iterrows():
            sym = row[1][0]
            # buy = row[1][1]
            shares = row[1][1]

            i_col = price2.columns.get_loc(sym + "_n")

            # if buy == "BUY":
            if i == 0:
                if row_num == 0:
                    price2.iat[i, i_col] = shares
                else:
                    price2.iat[i, i_col] = price2.iloc[i, i_col] + shares

            else:
                if row_num == 0:
                    price2.iat[i, i_col] = price2.iloc[i - 1, i_col] + shares
                else:
                    price2.iat[i, i_col] = price2.iloc[i, i_col] + shares

            if shares != 0:
                price2.iat[i, -2] = price2.iloc[i, -2] - shares * price2.iloc[i][sym] * (1 + impact) - commission
            # else:
            #     if i == 0:
            #         if row_num == 0:
            #             price2.iat[i, i_col] = -shares
            #         else:
            #             price2.iat[i, i_col] = price2.iloc[i, i_col] - shares
            #     else:
            #         if row_num == 0:
            #             price2.iat[i, i_col] = price2.iloc[i - 1, i_col] - shares
            #         else:
            #             price2.iat[i, i_col] = price2.iloc[i, i_col] - shares
            #
            #     price2.iat[i, -2] = price2.iloc[i, -2] + shares * price2.iloc[i][sym] * (1 - impact) - commission

            row_num += 1

            total_value = 0
            for s in symbols:
                total_value += price2.iloc[i][s] * price2.iloc[i][s + "_n"]
            price2.iat[i, -1] = total_value + price2.iloc[i, -2]

    result = price2['value']

    return result


