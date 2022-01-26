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
    # Handle --input and --header. Import data and store in pandas dataframe.
    df = pd.read_csv(args.input, sep=' ', header=('infer' if args.header else None))
    print(df)

    # Handle --columns. Filter data on list of columns.
    if args.columns:
        df = df.iloc[:,args.columns]

    print(df)

    # Create plot and plot all columns.
    nbr_columns = df.shape[1]
    nbr_rows = df.shape[0]
    for col in range(0, nbr_columns):
        plt.scatter(range(nbr_rows), df.iloc[:,col])

    # Handle --show. Show plot.
    if args.show:
        print("Showing")
        plt.show()
    
    # Handle --output. Save figure in output file.
    if args.output:
        plt.savefig(args.output, dpi=300)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flexible command line tool for plotting. Uses matplotlib.")

    # Required positional argument
    parser.add_argument("-i", "--input", type=str, required=True)

    parser.add_argument("-f", "--filter", help="Filter out rows based on the argument.")
    parser.add_argument("-c","--columns", type=int, nargs='+', help="Plot only selected columns.", default=[])

    parser.add_argument("-o", "--output", type=str, help="Save plot in specified output file.")
    parser.add_argument("-s", "--show", help="Show plot after creation.", action='store_true')
    parser.add_argument("-he", "--header", help="Use this is data has header row", action='store_true')

    args = parser.parse_args()
    main(args)
