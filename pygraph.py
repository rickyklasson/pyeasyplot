#!/bin/python3
import argparse
import matplotlib



def main(args):
    pass



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flexible command line tool for plotting. Uses matplotlib.")

    # Required positional argument
    parser.add_argument("input", type=str)

    parser.add_argument("-f", "--filter", help="Filter on a specified column, column indexing starts at 0.")

    parser.add_argument("-s", "--save", help="Save plots. Will use header of columns as filename.")

    args = parser.parse_args()
    main(args)
