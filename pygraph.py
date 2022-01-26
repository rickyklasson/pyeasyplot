#!/bin/python3
from matplotlib import pyplot as plt
import argparse
import matplotlib
import pandas as pd

# Avoid display output issue when running over ssh.
matplotlib.use('Agg')


"""
    Wishlist for plotting features:
    - Simple command line command for creating and saving a plot.
    - Options for only plotting based on a filter column in input data. E.g. I and P-frames separate.
    - Options for plotting certain columns.
    - Options for handling header row.

    Prerequisites:
    - Data should be formatted in columns.
    - Packages: matplotlib etc...

    Implementation steps:
    1. Create an MVP where all columns are plotted in same graph.
    2. Extend to allow selection of columns to be plotted.
    3. Extend to allow filters to work.

    Pipeline:
    1. Import data and place in a pandas dataframe.
    2. Filter out the columns that we want to plot.
    3. Filter out the rows to be plotted.
"""

# Matplotlib setup.
plt.style.use('ggplot')
plt.figure(figsize=(16, 9))

def main(args):
    # Handle --input. Import data and store in pandas dataframe.
    df = pd.read_csv(args.input, sep=' ', header=None)

    # Handle --columns. Filter data if list of columns to plot is given.
    if args.columns:
        df = df.filter(items=args.columns, axis=1)

    # Create plot and plot all columns.
    nbr_columns = df.shape[1]
    nbr_rows = df.shape[0]
    for col in range(0, nbr_columns):
        plt.scatter(df.iloc[:,col], range(nbr_rows))

    plt.savefig('test.png', dpi=300)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flexible command line tool for plotting. Uses matplotlib.")

    # Required positional argument
    parser.add_argument("-i", "--input", type=str, required=True)

    parser.add_argument("-f", "--filter", help="Filter on a specified column, column indexing starts at 0.")
    parser.add_argument("-c","--columns", type=int, nargs='+', help='Plot only selected columns.', default=[])

    parser.add_argument("-s", "--save", help="Save plots. Will use header of columns as filename.")

    args = parser.parse_args()
    main(args)
