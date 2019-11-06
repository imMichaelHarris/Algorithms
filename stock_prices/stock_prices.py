#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # loop through prices and keep track of current min proce and the max profit
  max_profit_so_far = 0
  current_min_price_so_far = 0
  num_of_prices = 0
  while num_of_prices < len(prices):
    print(num_of_prices)
    num_of_prices += 1


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))