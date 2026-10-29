

numbers = [12, 45, 7, 23, 56, 89, 34, 90, 3, 67]
target = int(input(f"Enter a number to search from {numbers}: "))

checks = 0
found = False
for num in numbers:
    checks += 1
    if num == target:
        found = True
        break

print(f"\n--- Execution Results ---")
print(f"Target found: {found}")
print(f"Total checks performed: {checks}")

n = len(numbers)
print(f"\n--- Asymptotic Analysis (n = {n}) ---")
print(f"Best Case (Ω(1)): Found on the 1st check")
print(f"Average Case (Θ(n)): Expected ~{n // 2} checks")
print(f"Worst Case (O(n)): Up to {n} checks")