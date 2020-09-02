class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		total = 0
		win_max = 0
		i, j = 0, 0
		result = 0
		dic = defaultdict(int)

        while i < len(s) and j < len(s):
			dic[s[j]] += 1
			win_max = max(win_max, dic[s[j]])
			total += 1

			if total - win_max > k:
				total -= 1
				result = max(result, total)
				dic[s[i]] -= 1
				i += 1
			j += 1

		return max(total, result)