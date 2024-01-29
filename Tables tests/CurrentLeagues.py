import pandas as pd
from mwrogue.esports_client import EsportsClient
import time

def main():

    site = EsportsClient("lol")

    # Query the CurrentLeagues table for all leagues with a priority less than or equal to 10
    response = site.cargo_client.query(
        tables="CurrentLeagues",
        fields="Event",
        limit=500
    )

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Convert the response to a pandas DataFrame for better readability
    df = pd.DataFrame(response)

    # Log the fetched data
    print(df)

    #And write a csv
    df.to_csv("CurrentLeagues.csv", index=False)
    
    # Wait for 2 seconds before making the query
    time.sleep(2)

if __name__ == "__main__":
    main()



