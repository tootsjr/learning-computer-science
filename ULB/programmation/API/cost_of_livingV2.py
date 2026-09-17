from math import cos


class country:
    def __init__(self, salary, rent, cost_monthly):
        self.salary = salary
        self.rent = rent
        self.cost_monthly = cost_monthly

        salary = int(input("What is the average monthly salary of this country?: "))

    def cash_after_rent(self, salary, rent):
        cash_after_rent = salary - rent
        print(f"The cash you have left after rent is :{cash_after_rent}€")
        return cash_after_rent

    def savings(self, cash_after_rent, cost_monthly):
        savings = cash_after_rent - cost_monthly
        print(f"Here are your monthly savings : {savings}€")
        return savings


first_country = country()
