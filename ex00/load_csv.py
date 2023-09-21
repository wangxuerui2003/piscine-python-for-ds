import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
        Load a csv file into a pandas Dataframe.
        Return an empty Dataframe if error.
    """

    if not isinstance(path, str):
        print("Path must be a string!")
        return pd.DataFrame()  # df.empty == True

    extension = path.split('.')[-1]
    if not extension.lower() == 'csv':
        print("Input must be a csv file!")
        return pd.DataFrame()

    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except FileNotFoundError:
        print("CSV file not found!")
    except pd.errors.EmptyDataError:
        print("Empty dataset!")
    except pd.errors.ParserError:
        print("File Format error!")
    except Exception as e:
        print("Other error:", e)

    return pd.DataFrame()
