def knapsack(W, wt, val, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Input
n = int(input("Enter number of items: "))

val = []
wt = []

for i in range(n):
    val.append(int(input("Enter value of item " + str(i + 1) + ": ")))
    wt.append(int(input("Enter weight of item " + str(i + 1) + ": ")))

W = int(input("Enter capacity of knapsack: "))

# Calculate maximum value
result = knapsack(W, wt, val, n)

print("Maximum value =", result)
