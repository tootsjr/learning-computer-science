salary = float(input("Average monthly salary : "))
rent = float(input("Average monthly rent : "))
cost_monthly = float(
    input("Average amount you spend on shopping and utility monthly : ")
)


def cost_of_living(salary, rent, cost_monthly):
    cash_after_rent = salary - rent
    net_savings = cash_after_rent - cost_monthly

    print(
        f"Average monthly salary = {salary},\nAverage monthly rent = {rent},\nAverage monthly cash after rent = {cash_after_rent},\nAverage monthly cost of living = {cost_monthly},\nNet savings after everything = {net_savings}"
    )

    return 0


cost_of_living(salary, rent, cost_monthly)
