import pandas as pd
from itertools import combinations
import time
import datetime


class Actions:
    def __init__(self, input_file):
        self.input_file = input_file

    def best_result(self):
        start = time.time()
        df = pd.read_csv(self.input_file, sep=";")
        df.columns = ["action", "cost", "profit"]
        df["payout"] = ""
        df["profit"] = df["profit"].str.rstrip("%").astype(float) / 100
        df["payout"] = df["profit"] * df["cost"]
        max_combination = 2**len(df)
        number_combinations = 1
        best_payout = 0
        best_combination = []
        for size_combination in range(len(df)):
            for combination in combinations(df.values.tolist(),
                                            size_combination):
                combination = list(combination)
                sum_costs = 0
                sum_payout = 0
                for iCombination in combination:
                    sum_costs += iCombination[1]
                    sum_payout += iCombination[3]
                if sum_costs <= 500:
                    if sum_payout >= best_payout:
                        best_payout = sum_payout
                        best_combination = combination
                number_combinations += 1
                print(number_combinations, "/", max_combination)
        end = time.time()
        elapsed = end - start
        print("La meilleure combinaison est la suivante : ")
        print([action[0] for action in best_combination])
        print("pour un gain de ", best_payout, " euros")
        print("Temps de traitement : ", datetime.timedelta(seconds=elapsed))


file = "actions.csv"
instance_action = Actions(file)
instance_action.best_result()
