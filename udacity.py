import pandas as pd
import matplotlib.pyplot as plt


def get_max_close(symbol):
    """ Return the maximum closing values for stock indicated by symbol

    Note: Data for a stock is stored in file : data/<symbol>.csv
    """
    df = pd.read_csv("~Deepak/AlphaX/{}.csv".format(symbol))  # read in data
    return df['Close'].max()  # compute and return max


def get_mean_volume(symbol):

    df = pd.read_csv("~Deepak/AlphaX/{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()  # compute and return average


def plotchart(symbol):

    df = pd.read_csv("~Deepak/AlphaX/{}.csv".format(symbol))  # read in data
    df['Close'].plot()  # plot chart
    plt.show()

# def create_dataframe():
#     start_date = '2017-01-22'
#     end_date = '2018-01-22'
#     dates = pd.date_range(start_date,end_date)
#     df1 = pd.DataFrame(index=dates)


def test_run():
    # Define date range

    start_date = '2017-01-22'
    end_date = '2018-01-22'
    dates = pd.date_range(start_date, end_date)

    # Create an empty DataFrame
    df1 = pd.DataFrame(index=dates)

    # Read sbin data into temporary dataframe
    df_sbin = pd.read_csv("~Deepak/AlphaX/sbin.csv", index_col="Date",
                          parse_dates=True, usecols=['Date', 'Close'],
                          na_values=['nan'])
    # Rename 'Close' column to 'sbi' to prevent clash
    df_sbin = df_sbin.rename(columns={'Close': 'sbin'})

    # Join the two dataframes using DataFrame .join(),  with how = 'inner'
    df1 = df1.join(df_sbin, how='inner')

    # Read in more stocks
    symbols = ['kotakbank', 'nifty50']
    for symbol in symbols:
        df_temp = pd.read_csv("~Deepak/AlphaX/{}.csv".format(symbol),
                              index_col="Date",
                              parse_dates=True, usecols=['Date', 'Close'],
                              na_values=['nan'])

        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Close': symbol})
        df1 = df1.join(df_temp)  # use default how ='left'

    print(df1.head())

#     """Function called by Test Run."""
#     for symbol in ['sbin', 'kotakbank']:
#         print("Max Close")
#         print(symbol, get_max_close(symbol))
#         print("Mean Volume")
#         print(symbol, get_mean_volume(symbol))
#         print(plotchart(symbol))


if __name__ == "__main__":

    test_run()
