def stockMarket(nums):

  maxProfit, minPrice = 0, 0
  for price in nums:
    minPrice = min(price, minPrice)
    profit = price - minPrice
    maxProfit = max(maxProfit, profit)

  return maxProfit

print(stockMarket([7,1,5,3,6,4]))
