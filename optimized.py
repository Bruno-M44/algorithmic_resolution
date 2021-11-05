import time
import datetime
import pandas as pd


class Actions:
    def __init__(self, input_file):
        self.input_file = input_file

    def best_result(self):
        start = time.time()
        df = pd.read_csv(self.input_file, sep=",")
        df = df[df["price"] > 0]
        df["payout"] = ""
        df["payout"] = df["profit"] / 100 * df["price"]
        df = df.sort_values(by="price", ascending=False).reset_index(
            drop=True)
        df = pd.DataFrame([("Aucune action", 0, 0, 0)],
                          columns=df.columns).append(df, ignore_index=True)
        pd.DataFrame(["Aucune action", 0, 0])
        for costs_max in range(500 + 1):
            df[costs_max] = 0

        for iAction in range(1, len(df)):
            for costs_max in range(1, 500 + 1):
                if df.loc[iAction, "price"] <= costs_max:
                    df.loc[iAction, costs_max] = max(
                        df.loc[iAction - 1, costs_max],
                        df.loc[iAction, "payout"] +
                        df.loc[
                            iAction - 1, costs_max -
                            round(df.loc[iAction, "price"])])
                else:
                    df.loc[iAction, costs_max] = df.loc[iAction - 1, costs_max]

        best_combination = []
        sum_price = 0
        iAction = len(df) - 1
        costs_max = 500
        while iAction != 0 and costs_max != 0:
            if df.loc[iAction, costs_max] == df.loc[iAction, costs_max - 1]:
                costs_max -= 1
            elif df.loc[iAction, "payout"] + \
                    df.loc[iAction - 1, costs_max - round(df.loc[iAction,
                                                                 "price"])] \
                    >= df.loc[iAction - 1, costs_max]:
                best_combination.append((df.loc[iAction, "name"]))
                sum_price += df.loc[iAction, "price"]
                costs_max -= round(df.loc[iAction, "price"])
                iAction -= 1
            else:
                iAction -= 1

        end = time.time()
        elapsed = end - start
        print("La meilleure combinaison est la suivante : ")
        print(best_combination)
        print("pour un gain de ", df.iloc[-1][500], " euros")
        print("et un coût total de :", sum_price, " euros")
        print("Temps de traitement : ", datetime.timedelta(seconds=elapsed))
        # df.to_csv("df.csv", mode='w+')


dataset_part1 = "actions.csv"
instance_action = Actions(dataset_part1)
instance_action.best_result()

'''
dataset1 = "dataset1_Python+P7.csv"
instance_action = Actions(dataset1)
instance_action.best_result()
'''
