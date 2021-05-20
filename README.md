# superduper_crypto_crawler

to gather current snapshot of prices run:
python3 get_prices.py > crypto_data_snapshot.csv


to initiate live update run:
python3 live_update.py >> live_crypto_data.csv

to adjust how often data is gathered change update_interval_sec in live_update.py