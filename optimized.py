import time
import datetime
import pandas as pd


class Actions:
    def __init__(self, input_file):
        self.input_file = input_file

    def best_result(self):
        start = time.time()
        df = pd.read_csv(self.input_file, sep=";")
        df.columns = ["action", "cost", "profit"]
        df = df.sort_values(by="cost", ascending=False).reset_index(
            drop=True)
        df = pd.DataFrame([("Aucune action", 0, "0%")],
                          columns=df.columns).append(df, ignore_index=True)
        df["payout"] = ""
        df["profit"] = df["profit"].str.rstrip("%").astype(float) / 100
        df["payout"] = df["profit"] * df["cost"]
        pd.DataFrame(["Aucune action", 0, 0])
        for costs_max in range(500 + 1):
            df[costs_max] = 0

        for iAction in range(1, len(df)):
            for costs_max in range(1, 500 + 1):
                if df.loc[iAction, "cost"] <= costs_max:
                    df.loc[iAction, costs_max] = max(
                        df.loc[iAction - 1, costs_max],
                        df.loc[iAction, "payout"] +
                        df.loc[
                            iAction - 1, costs_max - df.loc[iAction, "cost"]])
                else:
                    df.loc[iAction, costs_max] = df.loc[iAction - 1, costs_max]

        best_combination = []
        for iAction in range(len(df) - 1, 1, -1):
            if df.loc[iAction, 500] != df.loc[iAction - 1, 500]:
                best_combination.append((df.loc[iAction, "action"]))
        best_combination

        end = time.time()
        elapsed = end - start
        print("La meilleure combinaison est la suivante : ")
        print(best_combination)
        print("pour un gain de ", df.iloc[-1][500], " euros")
        print("Temps de traitement : ", datetime.timedelta(seconds=elapsed))
        # df.to_csv("df.csv", mode='w+')


file = "actions.csv"
instance_action = Actions(file)
instance_action.best_result()
