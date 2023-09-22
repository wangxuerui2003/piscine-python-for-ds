import sys
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
        Main function
    """

    df = load('life_expectancy_years.csv')
    if df.empty is True:
        sys.exit()

    try:
        country_name = sys.argv[1] if len(sys.argv) >= 2 else "Malaysia"
        country = df[df['country'] == country_name]

        years = country.columns[1:]  # ignore the 'country' column
        values = country.iloc[0, 1:]  # ignore the <country_name> column
        years_ticks = []
        try:
            years_ticks = [year for year in years if int(year) % 40 == 0]
        except ValueError:
            print("Invalid years in csv!")
            sys.exit()

        # plotting
        plt.plot(years, values)
        plt.xticks(years_ticks)
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.title(f'{country_name} Life Expectancy Projections')
        plt.savefig('output.jpg')
    except IndexError:
        print("Country not found!")
    except KeyError:
        print("No country column in csv!")
    except Exception as e:
        print("Other error:", e)


if __name__ == '__main__':
    main()
