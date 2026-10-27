from collections import deque

def water_jug(capacity1, capacity2, target):
  visited = set()
  # The queue stores (jug1_amount, jug2_amount, path_taken)
  queue = deque()
  queue.append((0, 0, [])) # Starting state (0,0) with an empty path

  while queue:
    jug1, jug2, path = queue.popleft()

    # If this state has been visited, skip
    if (jug1, jug2) in visited:
      continue
    visited.add((jug1, jug2))

    current_path = path + [(jug1, jug2)] # Add current state to path

    # Check if target is reached
    if jug1 == target or jug2 == target:
      return current_path

    # Generate next possible states
    next_states = []

    # 1. Fill jug 1
    next_states.append((capacity1, jug2))
    # 2. Fill jug 2
    next_states.append((jug1, capacity2))
    # 3. Empty jug 1
    next_states.append((0, jug2))
    # 4. Empty jug 2
    next_states.append((jug1, 0))

    # 5. Pour jug1 to jug2
    pour_amount_jug1_to_jug2 = min(jug1, capacity2 - jug2)
    next_states.append((jug1 - pour_amount_jug1_to_jug2, jug2 + pour_amount_jug1_to_jug2))

    # 6. Pour jug2 to jug1
    pour_amount_jug2_to_jug1 = min(jug2, capacity1 - jug1)
    next_states.append((jug1 + pour_amount_jug2_to_jug1, jug2 - pour_amount_jug2_to_jug1))

    # Add valid next states to the queue
    for next_jug1, next_jug2 in next_states:
        if (next_jug1, next_jug2) not in visited:
            queue.append((next_jug1, next_jug2, current_path))

  return None # No solution found after exploring all states

# Main execution logic outside the function
jug1_cap = int(input("Enter the capacity of jug 1: "))
jug2_cap = int(input("Enter the capacity of jug 2: "))
target_vol = int(input("Enter the target volume: "))

solution = water_jug(jug1_cap, jug2_cap, target_vol)

if solution:
  print("\nSteps to reach the target:")
  for step in solution:
    print(step)
else:
  print("No solution found")