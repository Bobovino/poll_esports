from mwrogue.esports_client import EsportsClient
import pandas as pd
import time
from datetime import datetime

def main():

    site = EsportsClient("lol")

    game_id = 'North American Challengers League/2024 Season/Spring Season_Week 1_4_1'

    # Single query for both general game info and picks and bans
    response = site.cargo_client.query(
        tables="PicksAndBansS7",
        fields="Team1, Team2 , Winner, Team1Ban1, Team1Ban2, Team1Ban3, Team1Ban4, Team1Ban5, Team1Pick1, Team1Pick2, Team1Pick3, Team1Pick4, Team1Pick5, Team2Ban1, Team2Ban2, Team2Ban3, Team2Ban4, Team2Ban5, Team2Pick1, Team2Pick2, Team2Pick3, Team2Pick4, Team2Pick5, Team1PicksByRoleOrder,Team2PicksByRoleOrder",
        where=f"GameId='{game_id}'",
        limit=500
    )

    df = pd.DataFrame(response)
    df_game_info = df[['Team1', 'Team2', 'Winner']]
    df_picks_bans = df.drop(columns=['Team1', 'Team2', 'Winner'])

    # Set pandas display options
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Log the fetched data
    print(df_game_info)
    print(df_picks_bans.transpose())

    #And write a csv
    df_picks_bans.to_csv("PicksBans.csv", index=False)
    
    # Add a 2-second delay
    time.sleep(2)

if __name__ == "__main__":
    main()
