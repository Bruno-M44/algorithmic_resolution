import time
import pandas as pd


class Actions:
    def __init__(self, input_file):
        self.input_file = input_file

    def best_result(self):
        start = time.time()
        # df1 : Dataframe  en entrée
        # df2 : Dataframe résultats
        df1 = pd.read_csv(self.input_file, sep=";")
        df1.columns = ["action", "cost", "profit"]
        df1["payout"] = ""
        df1["profit"] = df1["profit"].str.rstrip("%").astype(float) / 100
        df1["payout"] = df1["profit"] * df1["cost"]
        df2 = pd.DataFrame(columns=df1.columns)
        sum_costs = 0
        while sum_costs <= 500:
            if len(df1) != 0:
                while df1.loc[df1["profit"] == df1["profit"].max()]["cost"]. \
                        values[0] + sum_costs > 500:
                    df1.drop(
                        df1.loc[df1["profit"] == df1["profit"].max()].index,
                        inplace=True)
                    if len(df1) == 0:
                        break
                if len(df1) == 0:
                    break
                sum_costs += \
                    df1.loc[df1["profit"] == df1["profit"].max()][
                        "cost"].values[0]
                if sum_costs <= 500:
                    df2 = pd.concat([df2, df1.loc[
                        df1["profit"] == df1["profit"].max()].head(1)])
                    df1.drop(
                        df1.loc[df1["profit"] == df1["profit"].max()].index,
                        inplace=True)

        end = time.time()
        elapsed = end - start
        print("La meilleure combinaison est la suivante : ")
        print(df2["action"].values)
        print("pour un gain de ", df2["payout"].sum(), " euros")
        print("Temps de traitement : ", elapsed, "secondes")


file = "actions.csv"
instance_action = Actions(file)
instance_action.best_result()
