import pandas as pd
from mwrogue.esports_client import EsportsClient
import time

def main():

    site = EsportsClient("lol")

    response = site.cargo_client.query(
        tables="TournamentRosters",
        fields="Team,Roles,RosterLinks",
        where="OverviewPage='2023 Season World Championship/Main Event'",
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
    df.to_csv("TournamentRosters.csv", index=False)
    
    # Add a 2-second delay
    time.sleep(2)

if __name__ == "__main__":
    main()
