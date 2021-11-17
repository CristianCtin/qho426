def movement():
  path = ["Move forward", 10, "Move Backward", 5,"Move left", 3, "Move right", 1]
  return path

def run():
  print("Moving...")
  path = movement()
  for i in range(0, len(path), 2):
    print(f"{path[i]} for {path[i+1]} steps")

#range(start, end, step)

run()