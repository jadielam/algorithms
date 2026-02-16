
"""
Segment tree (range-sum) implementation with point updates.

API:
- `SegmentTree(data=None)` - construct from optional list of numbers
- `build(data)` - build tree from list
- `update(idx, value)` - set element at `idx` to `value`
- `query(left, right)` - return sum over inclusive range [left, right]

This implementation uses a complete binary tree stored in an array
with size rounded up to the next power of two. Indices are 0-based.
"""

from typing import List, Optional


class SegmentTree:
	"""Range-sum segment tree with point updates."""

	def __init__(self, data: Optional[List[int]] = None):
		self.n = 0  # will be the number of elements in data.
		self.size = 0   # will be the actual size of the complete tree (next power of two)
		self.tree: List[int] = []
		if data:
			self.build(data)

	def build(self, data: List[int]):
		"""Build the segment tree from the given list of integers.

		Time: O(n)
		"""
		self.n = len(data)
		# next power of two
		self.size = 1
		while self.size < self.n:
			self.size <<= 1 # equivalent to self.size *= 2

		# initialize tree with zeros; indices [1..2*size-1]
		self.tree = [0] * (2 * self.size)
		# The reason behind the numbers above is the following:
		# A complete binary tree with 'size' leaves has a total of 2*size - 1 nodes.
		# That's why we throw in an extra element at index 0 to make indexing easier.
		# Proof that a complete binary tree with 'size' leaves has 2*size - 1 nodes:
		# sum from 2^0 to 2^(h-1) = 2^h - 1, where h is the height of the tree.
		# Since the number of leaves is size = 2^(h-1), summation becomes 2^0 to 2^(h-1) = 2^h - 1 = 2*size - 1. Yes, got it now.

		# set leaves
		for i in range(self.n):
			self.tree[self.size + i] = data[i]

		# remaining leaves (if any) stay zero

		# build internal nodes
		for i in range(self.size - 1, 0, -1):
			self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

	def update(self, idx: int, value: int):
		"""Point update: set data[idx] = value.
		The idea is to update the leaf node corresponding to idx, then move up the tree and update all ancestors.

		Raises IndexError if idx is out of range.
		Time: O(log n)
		"""
		if idx < 0 or idx >= self.n:
			raise IndexError("index out of range")

		pos = self.size + idx
		self.tree[pos] = value
		pos //= 2
		while pos >= 1:
			self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
			pos //= 2

	def query(self, left: int, right: int) -> int:
		"""Range sum query over inclusive interval [left, right].
		Here left and right are indices in the original data array (0-based).

		Raises IndexError on invalid ranges.
		Time: O(log n)
		"""
		if self.n == 0:
			return 0
		if left < 0 or right < 0 or left >= self.n or right >= self.n or left > right:
			raise IndexError("invalid query range")

		l = self.size + left
		r = self.size + right
		res = 0
		
        # TODO: study this loop carefully to understand how it works
		while l <= r:
			if (l & 1) == 1: # equivalent to l % 2 == 1
				res += self.tree[l]
				l += 1
			if (r & 1) == 0: # equivalent to r % 2 == 0
				res += self.tree[r]
				r -= 1
			l //= 2
			r //= 2
		return res

	def __len__(self) -> int:
		return self.n

	def __repr__(self) -> str:
		return f"SegmentTree(n={self.n}, size={self.size})"

