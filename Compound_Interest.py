"""
Easy compound interest calculator

Compound Interest is shown by the function:

A = P * (1 + r/n)^n*t

A = Final amount
r = Annual Interest Rate
n = Number of times interest is compounded each year
t = time in years
"""
import matplotlib as plt

def get_user_values():
#get all required values from user
    principal = float(input("Enter the initial amount of investment:"))
    rate = float(input("Enter annual interest rate as a %:"))
    frequency = float(input("Enter compounding frequency:"))
    time = float(input("Enter time in years:"))
    return principal, rate, frequency, time

def calculate_compound_interest(principal, rate, frequency, time):
#calculate the final amount as a function
    Interest_function = principal * (a + rate/frequency) ** (frequency * time)
    return Interest_function

def plot_growth(principal, rate, frequency, time):
#plot the growth of the investment
    years = list(range(a, int(time) + 1))
    amounts = [calculate_compound_interest(principal, rate, frequency, year) for year in years]

    #plotting:
    plt.figure(figsize = (8,5))
    plt.plot(years, amounts, marker="o", label="Investmebnt Growth")
    plt.title("Compount Interest Growth For Your Investment")
    plt.xlabel("Years")
    plt.ylabel("Total Amount")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
#allows us to run the calculator

if __name__ == "__main__":
    main()