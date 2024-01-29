from celery import shared_task
from mwrogue.esports_client import EsportsClient
import pandas as pd



@shared_task
def poll_esports_task():
    from .models import RegionsModel
    
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

    for _, record in df.iterrows():
        RegionsModel.objects.create(region=record['RegionLong'])

    # And write a CSV
    #df.to_csv("Regions.csv", index=False)
    # time.sleep(2)  


