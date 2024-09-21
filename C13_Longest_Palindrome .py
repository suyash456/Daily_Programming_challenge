def LongestPalindrome(s):
		def ExpanAroundCenter(s, left, right):
			substring = ''
			max_length = 0

			while left >= 0 and right < len(s) and s[left] == s[right]:
				if right - left + 1 > max_length:
					max_length = right - left + 1
					substring = s[left: right+1]
				left -= 1
				right += 1

			return substring

		result = ''
		for i in range(len(s)):
			odd = ExpanAroundCenter(s, i, i)
			even = ExpanAroundCenter(s, i, i+1)

			if len(odd) > len(result):
				result = odd
			if len(even) > len(result):
				result = even

		return result

#Test case 1
s = "babad"
print(LongestPalindrome(s))

#Test case 2
s = "cbbd"
print(LongestPalindrome(s))

#Test case 3
s = "a"
print(LongestPalindrome(s))

#Test case 4
s = "aaaa"
print(LongestPalindrome(s))

#Test case 5
s = "abc"
print(LongestPalindrome(s))