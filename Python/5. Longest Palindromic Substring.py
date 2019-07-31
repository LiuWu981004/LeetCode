# solution 1
class Solution:
  def longestPalindrome(self,s):
    palindrome = ''
    for i in range(len(s)):  # range产生的数字是从0 到len - 1 正好与字符串索引匹配
      len1 = self.getlongestpalindrome(s,i,i) #aba 型回文判断
      if len(len1) > len(palindrome):
        palindrome = len1
      len2 = self.getlongestpalindrome(s,i,i+1) # aa型回文判断
      if len(len2) > len(palindrome):
        palindrome = len2
     return palindrome
         
  def getlongestpalindrome(self,s,l,r):
    #找出回文片段
    while l >=0 and r < len(s) and s[l] == s[r]:  #回文条件
      l -= 1
      r += 1
     return s[l+1:r] # 此时 l和r都进行了数值操作 而且与索引匹配， 左开右闭，l则需加一，r无需操作。

  
  # solution 2
class Solution:
   def longestPalindrome(self,s):
      palindrome = ''
      i = 0
      while i < len(s): # for循环中i只能按照for的结构进行增减  while循环则可以在循环中操作i的任意增减
        r,l = i, i
        while s[r] == s[r+1] and r+1 < len(s):  #判断中心是否是相同的数字，如此便可以区分开回文方式 中间相等，中间不相等
          r = i + 1
        i = r+1
        len1 = self.getlongestpalindrome(s,l,r)
        if len(len1) >len(palindrome):
          palindrome = len1
      return palindrome
        
    def getlongestpalindrome(self,s,l,r):
      while s[l] == s[r] and l>=0 and r<len(s):
        l-=1
        r+=1
      return s[l+1:r]   
      
