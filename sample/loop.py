profits = [200, 400, 90, 50, 20, 150]

filtered_profits = []

for p in profits:
    if p >= 100:
        filtered_profits.append(p)

print(filtered_profits)