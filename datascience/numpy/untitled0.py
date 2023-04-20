from typing import List

# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  total_discs_inflated = 0
  for i in range(1, N+1):
      inflatable_disc = R[i-1]
      
      if inflatable_disc > i:
          total_discs_inflated = total_discs_inflated + 1
      elif inflatable_disc < i:
          return -1
      
      if inflatable_disc > i and i ==N:
          
          total_discs_inflated = total_discs_inflated -1
          
  return total_discs_inflated;

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.


if __name__ == "__main__":
  k_1 = 5
  arr_1 = [60, 120, 140, 80, 90]

  output_1 = getMinimumDeflatedDiscCount( k_1,arr_1)

  print(output_1)

  # Add your own test cases here
  