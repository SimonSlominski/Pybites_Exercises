"""
NAME: Bite 281. Generating sales reports from Github data

In this bite you will learn how to process the output from a Github API
call and generate a summary sales report along with a yearly one.
It’s up to you to decide how to approach this bite,
with the exception of having to create a Pandas DataFrame from the data.

Summary Report

The summary report that you will generate will look like this by default:

                    sum          mean        max
        year
        2013  484247.51  40353.959167   81777.35
        2014  470532.51  39211.042500   75972.56
        2015  608473.83  50706.152500   97237.42
        2016  733947.03  61162.252500  118447.83

I’ve provided the global variable STATS, which is a list with sum, mean, max in it.
This is what controls what is included in the summary report.
That being said, the summary_report() function will include the optional stats variable,
which should default to STATS.

Yearly Report

The yearly report should be as follows, for example:

        2013
                  sales
        month
        1      14236.90
        2       4519.89
        3      55691.01
        4      28295.35
        5      23648.29
        6      34595.13
        7      33946.39
        8      27909.47
        9      81777.35
        10     31453.39
        11     78628.72
        12     69545.62
The yearly_report() function, along with requiring the DataFrame to work from,
takes a year variable which determines which year to report on.
If the given year is not included in the report, a ValueError should be raised.

For example, lets say that the year 1800 was passed, the error message should be:
"The year 1800 is not included in the report!"
"""

import json
import sys
import io
import os
from pathlib import Path
from typing import Dict, List, Union

import pandas as pd  # type: ignore
import requests

URL: str = "https://bites-data.s3.us-east-2.amazonaws.com/MonthlySales.csv"
STATS: List[str] = ["sum", "mean", "max"]
TMP: Path = Path(os.getenv("TMP", "/tmp")) / "MonthlySales.csv"

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)

def get_data(url: str) -> Dict[str, str]:
    """ Get data from Github
    Args:       url (str): The URL where the data is located.
    Returns:    Dict[str, str]: The dictionary extracted from the data
    """
    if TMP.exists():
        data = json.loads(TMP.read_text())
    else:
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.text)
        with TMP.open("w") as tmp:
            json.dump(data, tmp)
    return data

def process_data(url: str) -> pd.DataFrame:
    """ Process the data from the Github API
    Args:       url (str): The URL where the data is located.
    Returns:    pd.DataFrame: Pandas DataFrame generated from the processed data
    """
    content = requests.get(url).content
    data = pd.read_csv(io.StringIO(content.decode('utf-8')))
    return data

def summary_report(df: pd.DataFrame, stats: Union[List[str], None] = STATS) -> None:
    """Summary report generated from the DataFrame and list of stats

    Will aggregate statistics for sum, mean, and max by default.

    Args:
        df (pd.DataFrame): Pandas DataFrame of the Github API data
        stats (List[str], optional): List of summaries to aggregate. Defaults to STATS.
    Returns:
        None (prints to standard output)

        Example:
                    sum          mean        max
        year
        2013  484247.51  40353.959167   81777.35
        2014  470532.51  39211.042500   75972.56
        2015  608473.83  50706.152500   97237.42
        2016  733947.03  61162.252500  118447.83
    """
    url_data = 'https://raw.githubusercontent.com/bsullins/data/master/MonthlySales.csv'
    df = process_data(url_data)
    # convert column 'month' to datetime
    df['month'] = pd.to_datetime(df['month'])
    years = df['month'].dt.year

    ret = df.groupby(df['month'].dt.year)['sales'].agg(STATS)
    ret = ret.rename_axis('year')

    print(ret, file=sys.stdout)
    print(type(ret))




url_data = 'https://raw.githubusercontent.com/bsullins/data/master/MonthlySales.csv'
test_report = summary_report(process_data(url_data))
print(test_report)

def yearly_report(df: pd.DataFrame, year: int) -> None:
    """Generate a sales report for the given year

    Args:
        df (pd.DataFrame): Pandas DataFrame of the Github API data
        year (int): The year to generate the report for

    Raises:
        ValueError: Error raised if the year requested is not in the data.
        Should be in the form of "The year YEAR is not included in the report!"

    Returns:
        None (prints to standard output)

        Example:
        2013
                  sales
        month
        1      14236.90
        2       4519.89
        3      55691.01
        4      28295.35
        5      23648.29
        6      34595.13
        7      33946.39
        8      27909.47
        9      81777.35
        10     31453.39
        11     78628.72
        12     69545.62
    """
    pass


# uncomment the following for viewing/testing the reports/code
# if __name__ == "__main__":
#     data = process_data(URL)
#     summary_report(data)
#     for year in (data["month"].dt.year).unique():
#         yearly_report(data, year)

#     yearly_report(data, 2020)