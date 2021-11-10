import time
import datetime
import pandas as pd
from math import *


def df_filling(df, max_price):
    """Function of filling of Dataframe of optimized solutions.
        Parameters
        ----------
        df : Dataframe
            Dataframe initialized.
        max_price : int
            Price not to be exceeded.

        Returns
        -------
        Dataframe
            Dataframe filled.
    """
    df = df.reset_index(drop=True)
    for price_limit in range(max_price + 1):
        df[price_limit] = 0

    for iAction in range(1, len(df)):
        for price_limit in range(1, max_price + 1):
            if df.loc[iAction, "price"] <= price_limit:
                df.loc[iAction, price_limit] = max(
                    df.loc[iAction - 1, price_limit],
                    df.loc[iAction, "payout"] +
                    df.loc[
                        iAction - 1, floor(price_limit -
                                           df.loc[iAction, "price"])])
            else:
                df.loc[iAction, price_limit] = df.loc[iAction - 1, price_limit]
    return df


def get_results(df, max_price):
    """Function to get results from the Dataframe of optimized solutions.
        Parameters
        ----------
        df : Dataframe
            Dataframe filled.
        max_price : int
            Price not to be exceeded.

        Returns
        -------
        Dataframe
            Dataframe with the selected lines.
    """
    df_results = pd.DataFrame(columns=df.columns)
    iAction = len(df) - 1
    price_limit = max_price
    while iAction != 0 and price_limit != 0:
        if df.loc[iAction, price_limit] == df.loc[iAction, price_limit - 1]:
            price_limit -= 1
        elif df.loc[iAction, "payout"] + \
                df.loc[iAction - 1, price_limit - floor(df.loc[iAction,
                                                               "price"])] \
                >= df.loc[iAction - 1, price_limit]:
            df_results = df_results.append(df.loc[iAction])
            price_limit -= ceil(df.loc[iAction, "price"])
            iAction -= 1
        else:
            iAction -= 1

    return df_results


class Actions:
    """Class with input the file of actions with the rows name, price, profit.
    """
    def __init__(self, input_file):
        """Function of initialization.
            Parameters
            ----------
            input_file : str
                file name in the repertory.
        """
        self.input_file = input_file

    def df_init(self):
        """Function to initialize the Dataframe of optimized solutions.
            Returns
            -------
            Dataframe
                Dataframe initialized.
        """
        df = pd.read_csv(self.input_file, sep=",")
        df = df[df["price"] > 0]
        df["payout"] = ""
        df["payout"] = df["profit"] / 100 * df["price"]
        df = df.sort_values(by="price", ascending=False).reset_index(
            drop=True)
        df = pd.DataFrame([("Aucune action", 0, 0, 0)],
                          columns=df.columns).append(df, ignore_index=True)
        pd.DataFrame(["Aucune action", 0, 0])

        return df

    def best_result(self):
        """Function to get the Dataframe with optimized solutions and display
        the selected solution.
        """
        start = time.time()
        df = self.df_init()

        total_payout = 0
        best_combination = []
        sum_price = 0
        max_price = 500

        while max_price >= \
                df.loc[df["name"] != "Aucune action"]["price"].min():
            df = df_filling(df, max_price)

            total_payout += df.iloc[-1][max_price]
            df_results = get_results(df, max_price)
            best_combination.extend(df_results["name"].tolist())
            sum_price += df_results["price"].sum()
            max_price -= ceil(df_results["price"].sum())
            # df.to_csv("df.csv", mode='w+')
            df = df.drop(df_results.index)

        end = time.time()
        elapsed = end - start
        print("La meilleure combinaison est la suivante : ")
        print(best_combination)
        print("pour un gain de ", total_payout, " euros")
        print("et un coût total de :", sum_price, " euros")
        print("Temps de traitement : ", datetime.timedelta(seconds=elapsed))


print("SOLUTION POUR LE FICHIER 'actions.csv' :")
dataset_part1 = "actions.csv"
instance_action = Actions(dataset_part1)
instance_action.best_result()


print("SOLUTION POUR LE FICHIER 'dataset1_Python+P7.csv' :")
dataset1 = "dataset1_Python+P7.csv"
instance_action = Actions(dataset1)
instance_action.best_result()


print("SOLUTION POUR LE FICHIER 'dataset2_Python+P7.csv' :")
dataset2 = "dataset2_Python+P7.csv"
instance_action = Actions(dataset2)
instance_action.best_result()
