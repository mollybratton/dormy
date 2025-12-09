import argparse
from ProductionCode.helper_functions import *
from ProductionCode.datasource import *

data = DataSource()
def main():
    parser = argparse.ArgumentParser(prog='PROG', usage = "Usage statement: python3 command_line.py --ses 'county_name' or python3 command_line.py --scores 'county_name'")

    parser.add_argument("--ses", type = str)
    parser.add_argument("--scores", type = str)


    args = parser.parse_args()

    if (args.ses == "") or (args.scores == ""):
        print("Usage statement: python3 command_line.py --ses 'countyname' or python3 command_line.py --scores 'countyname'")

    else:
        if args.ses:
            print(data.getSESByCounty(args.ses))

        if args.scores:
            print(data.getScoresByCounty(args.scores))

if __name__ == "__main__":
    main()



