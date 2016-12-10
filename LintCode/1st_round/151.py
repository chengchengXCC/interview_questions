class Solution:
	def maxProfit(self, prices):
		if len(prices) == 0 or len(prices) == 1:
			return 0
		left = [0 for i in range(len(prices))]
		right = [0 for i in range(len(prices))]
		min_v = prices[0]
		for i in range(1, len(prices)):
			min_v = min(prices[i], min_v)
			left[i] = max(left[i - 1], prices[i] - min_v)
		max_v = prices[len(prices) - 1]
		right[len(prices) - 1] = 0
		i = len(prices) - 2
		while i >= 0:
			max_v = max(prices[i], max_v)
			right[i] = max(right[i + 1], max_v - prices[i])
			i -= 1
		profit = 0
		for i in range(0, len(prices)):
			if left[i] + right[i] > profit:
				profit = left[i] + right[i]
		return profit

