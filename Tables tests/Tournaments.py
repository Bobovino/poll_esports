import pandas as pd
from mwrogue.esports_client import EsportsClient
import time
from datetime import datetime

def main():

    site = EsportsClient("lol")

    # Get the current year
    current_year = datetime.now().year-1

    # Query to get data for tournaments where region is International or EMEA and the year is the current year
    response = site.cargo_client.query(
        tables="Tournaments",
        fields="Name, DateStart, EventType, TournamentLevel, OverviewPage , Rulebook",
        where=f"Region='International'  AND Year='{current_year}' ",
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
    df.to_csv("Tournaments.csv", index=False)
    
    # Add a 2-second delay
    time.sleep(2)

if __name__ == "__main__":
    main()

