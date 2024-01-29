import pandas as pd
from mwrogue.esports_client import EsportsClient
import time
from datetime import datetime

def main():

    site = EsportsClient("lol")

    match_id = 'LEC/2024 Season/Winter Season_Week 3_8'


    response = site.cargo_client.query(
        tables="MatchScheduleGame",
        fields="OverviewPage,GameId, Selection,Blue, Red, Winner ",
        where=f"MatchId='{match_id}'",
        limit=500
    )

    # Convert the response to a Pandas DataFrame for a readable output
    df = pd.DataFrame(response)

    # Set pandas display options
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Log the fetched data
    print(df)

    #And write a csv
    df.to_csv("GameSeries.csv", index=False)
    
    # Add a 2-second delay
    time.sleep(2)

if __name__ == "__main__":
    main()
