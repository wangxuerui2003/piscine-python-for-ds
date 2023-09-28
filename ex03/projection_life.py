import sys
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
        Main function
    """

    le = load('../life_expectancy_years.csv')
    if le.empty is True:
        sys.exit()

    income = load(
        '../income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    if income.empty is True:
        sys.exit()

    try:
        le = le['1900']
        income = income['1900']

        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")  # to make the graph looks the same as pdf
        plt.scatter(income, le)
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

        plt.savefig('output.jpg')
    except IndexError:
        print("Country not found!")
    except KeyError:
        print("No country column in csv!")
    except Exception as e:
        print("Other error:", e)


if __name__ == '__main__':
    main()
