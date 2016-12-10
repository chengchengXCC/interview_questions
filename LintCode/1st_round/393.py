class Solution:
	"""
	@param k: an integer
	@param prices: a list of integer
	@return: an integer which is maximum profit
	"""
	def maxProfit(self, k, prices):
		if k == 0:
			return 0
		maxPro = 0
		if k >= len(prices) / 2:
			for i in range(1, len(prices)):
				if prices[i] > prices[i - 1]:
					maxPro += prices[i] - prices[i - 1]
			return maxPro

		mustSell = []
		for i in range(0, len(prices)):
			mustSell.append([])
			for j in range(0, k + 1):
				mustSell[i].append(0)
		globalBest = []
		for i in range(0, len(prices)):
			globalBest.append([])
			for j in range(0, k + 1):
				globalBest[i].append(0)
		for i in range(0, k + 1):
			mustSell[0][i] = 0
			globalBest[0][i] = 0
		for i in range(1, len(prices)):
			mustSell[i][0] = 0
			diff = prices[i] - prices[i - 1]
			for j in range(0, k + 1):
				mustSell[i][j] = max(globalBest[i - 1][j - 1] + diff, mustSell[i - 1][j] + diff)
				globalBest[i][j] = max(globalBest[i - 1][j], mustSell[i][j])
		return globalBest[n - 1][k]


