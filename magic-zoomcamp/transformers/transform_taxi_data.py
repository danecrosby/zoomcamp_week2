import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(f"Preprocessing rows with zero passengers: { data[['passenger_count']].isin([0]).sum() }")
    data = data[data['passenger_count'] > 0]

    print(f"Preprocessing rows with zero distance trips: { data[['trip_distance']].isin([0]).sum() }")
    data = data[data['trip_distance'] > 0]

    #data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    data = data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'rate_code_ID',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    })

    return data

@test
def test_output(output, *args):
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with no distance'
    #assert not any(output['vendor_id'].isin([1,2])), 'There are unexpected vendor IDs'
    