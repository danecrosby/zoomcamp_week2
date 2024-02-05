import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    # select which months to read and concat
    start_month = 10
    end_month = 12

    # init empty dataframe
    dfs = []

    # green taxi data types
    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }

    # parsing by date
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']


    # loop from month # to month #
    for i in range(start_month, end_month + 1):
        file_path = f'green_tripdata_2020-{i}.csv.gz'
        print(f'Reading and adding {file_path} to the dataframe')

        dfs.append(pd.read_csv(file_path, compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates))

    # concatenate monthly data
    concatenated_df = pd.concat(dfs, ignore_index=True)

    return concatenated_df




@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
