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
    print("------ RAW DATAFRAME ------\n")
    print(df)

    # Handle --filter. Filter data on column and filter value.
    if args.filter:
        filter_idx = int(args.filter[0])
        filter_value = args.filter[1]
        
        # Do the filtering.
        df = df.loc[df.iloc[:, filter_idx] == filter_value]

    # Handle --columns. Filter data on list of columns.
    if args.columns:
        df = df.iloc[:,args.columns]
    
    print("\n\n------ FILTERED DATAFRAME ------\n")
    print(df)

    # Handle --preview. Only previewing data.
    if args.preview:
        return

    # Create plot and plot all columns.
    nbr_columns = df.shape[1]
    x_axis = df.index
    for col in range(0, nbr_columns):
        # Handle --graph-type, scatter or line.
        if args.graph_type == 'line':
            plt.plot(x_axis, df.iloc[:,col], alpha=1)
        else:
            # Default to scatter plot.
            plt.scatter(x_axis, df.iloc[:,col], s=4, alpha=1)

    # Handle --xlabel, --ylabel and --title. Setup legends and labels.
    plt.legend(list(df))
    plt.xlabel(args.xlabel)
    plt.ylabel(args.ylabel)
    plt.title(args.title)

    # Handle --show. Show plot.
    if args.show:
        plt.show()
    
    # Handle --output. Save figure in output file.
    if args.output:
        plt.savefig(args.output, dpi=300)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flexible command line tool for plotting. Uses matplotlib.")

    # Required positional argument
    parser.add_argument("-i", "--input", type=str, required=True, help="Input data for plot. Should be space-separated columns of data. See -he for info on headers.")

    parser.add_argument("-f", "--filter", type=str, nargs=2, help="Filter out rows based on a column and a value. E.g."
            + " : --filter 1 P filters out rows where column 1 has the value P.", metavar=('COLUMN', 'FILTER_VAL'))
    parser.add_argument("-c","--columns", type=int, nargs='+', help="Plot only selected columns.", default=[])

    parser.add_argument("-o", "--output", type=str, help="Save plot in specified output file.")
    parser.add_argument("-s", "--show", help="Show plot after creation.", action='store_true')
    parser.add_argument("-p", "--preview", help="Preview data in dataframe. Will not save nor show if set.", action='store_true')
    parser.add_argument("-he", "--header", help="Use this is data has header row", action='store_true')
    parser.add_argument("-x", "--xlabel", type=str, help="X-axis label")
    parser.add_argument("-y", "--ylabel", type=str, help="Y-axis label")
    parser.add_argument("-t", "--title", type=str, help="Plot title")
    parser.add_argument("-g", "--graph-type", type=str, help="Type of graph. (scatter or line)")

    args = parser.parse_args()
    main(args)
