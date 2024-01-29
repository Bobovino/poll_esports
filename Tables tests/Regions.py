from mwrogue.esports_client import EsportsClient
import pandas as pd
import time

def main():
    site = EsportsClient("lol")

    response = site.cargo_client.query(
        tables="Regions",
        fields="RegionLong",
        where="IsCurrent=1"
    )

        # Set pandas display options
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Convert the response to a Pandas DataFrame for a readable output
    df = pd.DataFrame(response)
        # Log the fetched data
    print(df)

    #And write a csv
    df.to_csv("Regions.csv", index=False)

    time.sleep(2)  # Add a 2-second delay

if __name__ == "__main__":
    main()
