import pandas as pd
from itertools import combinations
import time
import datetime


class Actions:
    def __init__(self, input_file):
        self.input_file = input_file

    def best_result(self):
        start = time.time()
        df = pd.read_csv(self.input_file, sep=",")
        df["payout"] = ""
        df["payout"] = df["profit"] / 100 * df["price"]
        max_combination = 2**len(df)
        number_combinations = 1
        best_payout = 0
        sum_price_final = 0
        best_combination = []
        for size_combination in range(len(df)):
            for combination in combinations(df.values.tolist(),
                                            size_combination):
                combination = list(combination)
                sum_price = 0
                sum_payout = 0
                for iCombination in combination:
                    sum_price += iCombination[1]
                    sum_payout += iCombination[3]
                if sum_price <= 500:
                    if sum_payout >= best_payout:
                        best_payout = sum_payout
                        best_combination = combination
                        sum_price_final = sum_price
                number_combinations += 1
                print(number_combinations, "/", max_combination)
        end = time.time()
        elapsed = end - start
        print("La meilleure combinaison est la suivante : ")
        print([action[0] for action in best_combination])
        print("pour un gain de ", best_payout, " euros")
        print("et un coût total de :", sum_price_final, " euros")
        print("Temps de traitement : ", datetime.timedelta(seconds=elapsed))


file = "actions.csv"
instance_action = Actions(file)
instance_action.best_result()
