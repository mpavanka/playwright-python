# Step 1: read once into memory
with open("./python-Concepts/test.txt", "r") as f:
    lines = f.readlines()

# Step 2: print
for line in lines:
    print(line)

# Step 3: write back
with open("./python-Concepts/test.txt", "a") as t:   # 'w' wipes, but we still have lines
    for line in lines:
        t.write("line" + "\n")

# Step 4: verify
with open("./python-Concepts/test.txt", "r") as f:
    for line in f:
        print(line)
