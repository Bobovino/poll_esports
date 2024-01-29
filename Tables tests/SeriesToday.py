import pandas as pd
from mwrogue.esports_client import EsportsClient
import time
from datetime import datetime, timedelta

def main():

    site = EsportsClient("lol")

    now = datetime.utcnow()
    three_hours_before = now - timedelta(hours=3)
    next_24_hours = now + timedelta(hours=24)

    response = site.cargo_client.query(
        tables="MatchSchedule",
        fields="DateTime_UTC, MatchId,  Team1, Team2, Round, Phase, BestOf, Patch, DisabledChampions, OverviewPage ",
        where=f"DateTime_UTC >= '{three_hours_before}' AND DateTime_UTC <= '{next_24_hours}'",
        limit=500
    )

    df = pd.DataFrame(response)

    # Set pandas display options
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Log the fetched data
    print(df)

    #And write a csv
    df.to_csv("SeriesToday.csv", index=False)
    
    # Add a 2-second delay
    time.sleep(2)

if __name__ == "__main__":
    main()



