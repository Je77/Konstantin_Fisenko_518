from math import pow,ceil,log,floor
import argparse


parser = argparse.ArgumentParser(description="Credit Calculator Project")
parser.add_argument('--type', help="Type of Payment (Annuity or Differential")
parser.add_argument('--payment', help="Monthly payment", type=int)
parser.add_argument('--principal', help="Credit principal", type=int)
parser.add_argument('--periods', help="Count of months", type=int)
parser.add_argument('--interest', help="Credit interest (rate of interest)", type=float)
args = parser.parse_args()


if args.type not in ['annuity', 'diff'] or args.type == 'diff' and args.payment != None:
    print('Incorrect Parameters')
    exit()

i = args.interest / (12 * 100)

if args.type == 'diff' and args.periods != None and args.principal != None and args.interest != None:
    count = 0
    for j in range(1, args.periods + 1):
        diff = ceil(args.principal / args.periods + i * (args.principal - (args.principal * (j - 1)) / args.periods))
        print(('Month {}: paid out {}').format(j, diff))
        count += diff
    print(f"\nOverpayment = {count - args.principal}")

elif args.type ==  "annuity":
    if args.periods != None and args.principal != None and args.interest != None:
        annuity = ceil(args.principal * (i * pow(1 + i, args.periods)) / (pow(1 + i, args.periods) - 1))
        print(f"Your annuity payment = {annuity}!\nOverpayment = {annuity * args.periods - args.principal}")
    elif args.periods != None and args.payment != None and args.interest != None:
        principal = floor(args.payment / (i * pow(1 + i, args.periods) / (pow(1 + i, args.periods) - 1)))
        print(f"Your loan principal = {principal}!\nOverpayment = {args.payment * args.periods - principal}")
