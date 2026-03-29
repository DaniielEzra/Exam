
user_inputs = []

while True:
    s = input("Enter a string (or type 'quit' to exit): ")

    if s.lower() == "quit":
        break

    user_inputs.append(s)

print("All entered strings:")
for item in user_inputs:
    print(item)

print(f"Total number of strings entered: {len(user_inputs)}")