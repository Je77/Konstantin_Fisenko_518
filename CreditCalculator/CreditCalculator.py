from math import pow,ceil,log,floor
import argparse


parser = argparse.ArgumentParser(description="Credit Calculator Project")
parser.add_argument('--type', help="Type of Payment (Annuity or Differential")
parser.add_argument('--payment', help="Monthly payment", type=int)
parser.add_argument('--principal', help="Credit principal", type=int)
parser.add_argument('--periods', help="Count of months", type=int)
parser.add_argument('--interest', help="Credit interest (rate of interest)", type=float)
args = parser.parse_args()


