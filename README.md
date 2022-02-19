# ETL-Get-current-playlist-from-Spotify
The ETL program helps fetch the current playlist of a user via Spotify API, which is scheduled to run via Airflow.

The ETL program is schduled to run in Airflow


![airflow_output](https://user-images.githubusercontent.com/84988205/154800591-768a1ac3-7150-421a-a8c4-176ac1cc9fc7.JPG)


The data is loaded into MongoDB, showing the playlist of the user. The data is loaded once in 24 hours, if available.

![mongodb_output](https://user-images.githubusercontent.com/84988205/154800771-503c501f-b61c-43d4-8f78-40fdb2586c80.JPG)
