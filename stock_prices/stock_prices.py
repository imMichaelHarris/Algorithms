#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # loop through prices and keep track of current min proce and the max profit
  # in loop subtract the min price from  item and if items larger than profit change profit
  max_profit_so_far = 0
  current_min_price_so_far = 0
  # num_of_prices = 0

  for i in prices:
    if i == prices[0]:
      current_min_price_so_far = i
    if max_profit_so_far <= i - current_min_price_so_far:
      max_profit_so_far = i - current_min_price_so_far
      print(f"max {max_profit_so_far}, {current_min_price_so_far}, {i}")
    if i == prices[-1] and max_profit_so_far == 0:
      print(f"last item {i}, {current_min_price_so_far}")
      max_profit_so_far = i - current_min_price_so_far
    if i < current_min_price_so_far:
      current_min_price_so_far = i

    print(f"min - {current_min_price_so_far}, max - {max_profit_so_far}, i - {i}")
  return max_profit_so_far
    # print(f"i is {i}, current min price is {current_min_price_so_far}")
  # while num_of_prices < len(prices) - 1:
  #   print(prices[num_of_prices], current_min_price_so_far)
  #   current_min_price_so_far = prices[num_of_prices]
  #   if prices[num_of_prices] < current_min_price_so_far:
  #     current_min_price_so_far = prices[num_of_prices]
  #   print("min price", prices[num_of_prices], current_min_price_so_far)
  #   num_of_prices += 1


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))