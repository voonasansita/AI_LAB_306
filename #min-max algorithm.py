#min-max algorithm
def minmax(depth, nodeindex, isMax, scores, height):
  # Base case: leaf node reached
  if depth == height:
    return scores[nodeindex]

  # Recursive case: internal node
  if isMax:
    return max(
        minmax(depth + 1, nodeindex * 2, False, scores, height),
        minmax(depth + 1, nodeindex * 2 + 1, False, scores, height)
    )
  else:
    return min(
        minmax(depth + 1, nodeindex * 2, True, scores, height),
        minmax(depth + 1, nodeindex * 2 + 1, True, scores, height)
    )

# main program
scores = list(map(int, input("enter 8 leaf nodes values:").split()))
height = 3 # For 8 leaf nodes, height of the tree is 3 (2^3 = 8)
result = minmax(0, 0, True, scores, height)
print("\nthe optimal value is:", result)
