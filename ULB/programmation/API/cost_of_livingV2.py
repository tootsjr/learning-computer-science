import math


class country:
    def __init__(self, salary, rent, cost_monthly):
        self.salary = salary
        self.rent = rent
        self.cost_monthly = cost_monthly

    def cash_after_rent(self, salary, rent):
        cash_after_rent = salary - rent
        print(f"The cash you have left after rent is :{cash_after_rent}€")
        return cash_after_rent

    def savings(self, cash_after_rent, cost_monthly):
        savings = cash_after_rent - cost_monthly
        print(f"Here are your monthly savings : {savings}€")
        return savings


first_country = country(
    int(input("What is the average salary of this country ?: ")),
    int(input("what is the average rent per month for a 50m flat")),
    int(input("What is spent monthly on average on groceries?: ")),
)
second_country = country(
    int(input("What is the average salary of this country ?: ")),
    int(input("what is the average rent per month for a 50m flat")),
    int(input("What is spent monthly on average on groceries?: ")),
)
