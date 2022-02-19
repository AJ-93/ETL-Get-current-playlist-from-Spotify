from extract_ETL import *
from transform import *
from pymongo import MongoClient

track_info_df = main()

if check_validity(track_info_df):
    print("checks passed, starting load")

    data_df = track_info_df
    data_dict = data_df.to_dict('records')

    conn = MongoClient(<<mongodb connection string>>)

    database = conn.spotify
    collection = database.spotify_current_playlist
    collection.insert_many(data_dict)

    print("Load completed Successfully")
