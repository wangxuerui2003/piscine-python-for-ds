import sys
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def convert_population(pop_str):
    """Convert string repr of population to numbers"""
    if 'B' in pop_str:
        return float(pop_str.replace('B', '')) * 1e9
    if 'M' in pop_str:
        return float(pop_str.replace('M', '')) * 1e6
    if 'k' in pop_str:
        return float(pop_str.replace('k', '')) * 1e3
    return float(pop_str)


def plot_country(df: pd.DataFrame, country_name: str):
    """
        Helper function
        To plot a single country
    """

    try:
        # get the populations row of a country
        country = df[df['country'] == country_name]

        # get all the years
        years = country.columns[1:]  # ignore the 'country' column

        # only retain the years that are within 1800 and 2050
        years = [y for y in years if int(y) >= 1800 and int(y) <= 2050]

        # get population values and ignore the <country_name> column
        values = country.iloc[0, 1:][:len(years)]

        # convert the population values into float
        populations = [convert_population(pop) for pop in values]

        plt.plot(years, populations, label=country_name)
    except ValueError:
        print("Invalid years in csv!")
        sys.exit()


def main():
    """
        Main function
    """

    df = load('../population_total.csv')
    if df.empty is True:
        sys.exit()

    try:
        country_name = "Malaysia"
        cmp_country_name = sys.argv[1] if len(sys.argv) >= 2 else "France"
        if cmp_country_name == "Malaysia":
            print("Cannot compare same countries!")
            sys.exit()

        plot_country(df, country_name)
        plot_country(df, cmp_country_name)

        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title("Population Projections")

        # only plot ticks that are 40 years away
        plt.xticks([str(year) for year in range(1800, 2050, 40)])

        # draw the same y-ticks as pdf does
        plt.yticks([20 * 1e6, 40 * 1e6, 60 * 1e6], ['20M', '40M', '60M'])

        plt.legend(loc='lower right')
        plt.savefig('output.jpg')

    except IndexError:
        print("Country not found!")
    except KeyError:
        print("No country column in csv!")
    except Exception as e:
        print("Other error:", e)


if __name__ == '__main__':
    main()
