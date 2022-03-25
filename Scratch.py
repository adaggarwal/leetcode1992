from itertools import product
from math import prod

'''
[1,2,3]

[1]

[2]

[2,2,2,2,2]

[0,1,-1,3,2]
'''

def test():
  runTest([2,3,4,5],[60,40,30,24])
  runTest([2],[1])
  
  
def runTest(i,e):
    obj = Solution()
    o = obj.productExceptSelf(i) 
    assert o == e
    print(f"Passed: i={i} o={o} e={e}")

class Solution:    
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    product = nums.copy()
    globProd = 1
    for i in range(1,len(nums)-1): 
      product[i] = product[i-1]*product[i]
    for i in range(len(nums)-1,-1,-1):
      product[i] = product[i-1]*globProd if i>0 else globProd
      globProd *= nums[i]
    return product 

if __name__ == '__main__':
  test()