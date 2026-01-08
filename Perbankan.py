# Data
items = ["A","B","C","D","E","F","G","H","I","J"]
weights = [4,3,5,6,2,7,4,1,5,3]
profits = [18,15,24,30,10,32,20,6,26,16]
capacity = 25
n = len(items)

# Tabel DP
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Proses Dynamic Programming
for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i-1] <= w:
            dp[i][w] = max(
                dp[i-1][w],
                dp[i-1][w - weights[i-1]] + profits[i-1]
            )
        else:
            dp[i][w] = dp[i-1][w]

# Backtracking untuk item terpilih
w = capacity
selected_items = []
total_cost = 0

for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected_items.append(items[i-1])
        total_cost += weights[i-1]
        w -= weights[i-1]

selected_items.reverse()

print("\n==============================")
print(" HASIL 0/1 KNAPSACK PERBANKAN ")
print("==============================")

print(f"Nilai maksimum (Return) : {dp[n][capacity]}")
print(f"Total biaya (Dana)      : {total_cost}")

print("\nDaftar item terpilih:")
for item in selected_items:
    idx = items.index(item)
    print(f"- Item {item} | Dana = {weights[idx]} | Return = {profits[idx]}")

