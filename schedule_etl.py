import airflow
from airflow import DAG
from datetime import timedelta,datetime
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
import os

tmpl_search_path = []

for subdir in ['tmpl_path'] :
    tmpl_search_path.append(os.path.join('/home/ajay/airflow',subdir))

default_args = {
    'owner' : 'ajay',
    'start_date' : datetime(2022,2,14),
    'email' : ['kc.ajay1993@gmail.com'],
    'email_on_failure' : True,
    'email_on_retry' : True,
    'retries' : 2,
    'retry_delay' : timedelta(minutes=5),
}

dag = DAG(
    dag_id='ETL_spotify_playlist',
    default_args=default_args,
    description='Getting spotify playlists',
    schedule_interval=timedelta(days=1),
    template_searchpath=tmpl_search_path,
)

extract = BashOperator(
    task_id='extract',
    bash_command='python3 /home/ajay/airflow/tmpl_path/extract_ETL.py',
    dag=dag,
)

transform_func = BashOperator(
    task_id='transform',
    bash_command='python3 /home/ajay/airflow/tmpl_path/transform.py',
    dag=dag,
)

load_func = BashOperator(
    task_id='load',
    bash_command='python3 /home/ajay/airflow/tmpl_path/load.py',
    dag=dag,
)

extract >> transform_func >> load_func
