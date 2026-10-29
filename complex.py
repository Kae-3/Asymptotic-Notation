
n = int(input("Enter value for n: "))

# O(1) - Constant Time
print("\n--- O(1) Constant Complexity ---")
steps = 1
print(f"Steps: {steps}")

print("\n--- O(n) Linear Complexity ---")
steps = 0
for i in range(n):
    steps += 1
print(f"Steps: {steps} (grows linearly with n)")

# O(n^2) - Quadratic Time
print("\n--- O(n^2) Quadratic Complexity ---")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print(f"Steps: {steps} (grows quadratically with n^2)")