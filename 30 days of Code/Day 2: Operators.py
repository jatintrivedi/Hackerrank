def solve(meal_cost, tip_percent, tax_percent):
    totalCost = 0
    tip_percent = (meal_cost * tip_percent) / 100
    tax_percent = (meal_cost * tax_percent) / 100
    totalCost = int(round(meal_cost + tip_percent + tax_percent))
    return totalCost

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
