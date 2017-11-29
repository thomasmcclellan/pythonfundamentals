# Review of 01-07

############
# Problem 1
############

# Given a lits of integers, return True if the sequence of numbers = 1,2,3 somewhere in the list

# i.e. arrayCheck([1,1,2,3,1]) => True
# i.e. arrayCheck([1,1,2,4,1]) => False
# i.e. arrayCheck([1,1,2,1,2,3]) => True

def arrayCheck(nums):
  for i in range(len(nums) - 2):
    if nums[1] == 1 and nums[1 + 1] == 2 and nums[1 + 2] == 3:
      return True
  return False

############
# Problem 2
############

# Given a strin, return a new string made of every other character starting with the first, so 'Hello' yields 'Hlo'.

# i.e. stringBits('Hello') => 'Hlo
# i.e. stringBits('Hi') => 'H'
# i.e. stringBits('Heeololeo') => 'Hello'

def stringBits(my_string):
  result = ''

  for i in range(len(my_string)):
    if i % 2 == 0:
      result += my_string[i]
  
  return result

  ############
  # Problem 3
  ############

  # Given two strings, return True if either of the strings appear at the very end of the other, ignoring upper/lower case differences

  # Note: s.lower() returns the lowercase version of a string

  # i.e. end_other('Hiabc', 'abc') => True
  # i.e. end_other('AbC', 'HiaBc) => True
  # i.e. end_other('abc', 'abXabc') => True

  def end_other(a,b):
    a = a.lower()
    b = b.lower()

    # return(b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-len(a):]

############
# Problem 4
############

# Given a string, return a string where for every character in the original, there are two characters

# i.e. double_char('The') => 'TThhee'
# i.e. double_char('AAbb') => 'AAAAbbbb'
# i.e. double_char('Hi-There') => 'HHii--TThheerree'

def double_char(my_string):
  result = ''

  for char in my_string:
    result += char * 2
  return result

############
# Problem 5
############

# Given 3 int values, a b c, return their sum
# However, if any of hte values is teen--in the range 13-19 inclusive--then that value counts as 0, except 15 and 16 do not count as a teen
# Write a separate helper 'def fix_teen(n):' that takes in an int value and returns that value fixed for the teen rule.

# In this way, you avoid repeating the teen code 3 times (i.e. 'decomposition').
# Define the helper below and at the same indent level as the main no_teen_sum()

# i.e. no_teen_sum(1,2,3) => 
# i.e. no_teen_sum(2,13,1) => 3
# i.e. no_teen_sum(2,1,14) => 3

def no_teen_sum(a,b,c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n [13,14,17,18,19]:
    return 0
  return n

############
# Problem 6
############

# Return the number of even integers in the given array

# i.e. count_evens([2,1,2,3,4]) => 3
# i.e. count_evens([2,2,0]) => 3
# i.e. count_evens([1,3,5]) => 0

def count_evens(nums):
  count = 0

  for element in nums:
    if element % 2 == 0: 
      count += 1
  return count