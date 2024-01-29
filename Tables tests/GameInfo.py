import pandas as pd
from mwrogue.esports_client import EsportsClient
from datetime import datetime
import time

def main():
    site = EsportsClient("lol")

    game_id = 'LEC/2024 Season/Winter Season_Week 2_13_1'

    # Query for MatchScheduleGame
    response_match_schedule_game = site.cargo_client.query(
        tables="MatchScheduleGame",
        fields="GameId, Selection, Blue, Red, Winner",
        where=f"GameId='{game_id}'",
        limit=500
    )
    df_match_schedule_game = pd.DataFrame(response_match_schedule_game)
    
    # 3-second delay
    time.sleep(3)

    # Query for PicksAndBansS7
    response_picks_bans = site.cargo_client.query(
        tables="PicksAndBansS7",
        fields="GameId, Team1, Team2, Winner, Team1Ban1, Team1Ban2, Team1Ban3, Team1Ban4, Team1Ban5, Team1Pick1, Team1Pick2, Team1Pick3, Team1Pick4, Team1Pick5, Team2Ban1, Team2Ban2, Team2Ban3, Team2Ban4, Team2Ban5, Team2Pick1, Team2Pick2, Team2Pick3, Team2Pick4, Team2Pick5, Team1PicksByRoleOrder, Team2PicksByRoleOrder",
        where=f"GameId='{game_id}'",
        limit=500
    )
    df_picks_bans = pd.DataFrame(response_picks_bans)

    # Merging the DataFrames on GameId
    merged_df = pd.merge(df_match_schedule_game, df_picks_bans, on='GameId')

    # Set pandas display options
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Displaying the merged DataFrame
    print(merged_df)

    #And write a csv
    merged_df.to_csv("GameInfo.csv", index=False)

    # 3-second delay
    time.sleep(3)

if __name__ == "__main__":
    main()
