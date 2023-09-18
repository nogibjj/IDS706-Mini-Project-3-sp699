# Main.py using polars and matplotlib to set data and see some plot

import polars as pl
import matplotlib.pyplot as plt


# Load the dataset from .csv file
def load_data():
    penguins_df = pl.read_csv("penguins.csv")
    print(penguins_df)
    return penguins_df


# Calculate mean, median, standard deviation of each columns
def calculate_stat():
    penguins_df = load_data()
    penguins_desc = penguins_df.describe()
    print(penguins_desc)


calculate_stat()


# Make a histogram of 'bill_length_mm' column in penguins.csv
def build_histogram():
    penguins_df = load_data()
    plt.hist(
        penguins_df["bill_length_mm"].to_pandas(),
        bins=20,
        color="green",
        edgecolor="white",
    )
    plt.xlabel("bill_length_mm")
    plt.ylabel("Frequency")
    plt.title("Bill Length Histogram")
    plt.savefig("bill_length_hist.png")
    plt.show()
    return


build_histogram()
