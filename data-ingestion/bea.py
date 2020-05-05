'''Code required to pull data from the BEA REST APIs

Attributes:
    BASE_URL (str): The base URL for the BEA API
'''


import datetime

import asyncio
import aiohttp


USER_ID = 'D8424480-1786-43F9-99B1-12CACEAF75AF'
BASE_URL = "https://apps.bea.gov/api/data/"


async def get_nipa_table_args(table_args):
    '''Get current table IDs for NIPA dataset
    '''

    params = {
        'UserID': USER_ID,
        'Method': 'GetParameterValues',
        'DatasetName': 'NIPA',
        'ParameterName': 'TableId'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.json()

    def clean_table_args(d):
        return {
            'frequency': 'M' if '(M)' in d['Description'] else 'Q',
            'table_name': d['TableName']
        }

    table_args.extend(map(clean_table_args, data['BEAAPI']['Results']['ParamValue']))


async def get_nipa_table_data(table_name, frequency, year=None):
    '''
    '''
    if year is None:
        today = datetime.date.today()
        year = today.year - 1

    params = {
        'UserID': USER_ID,
        'Method': 'GetData',
        'DatasetName': 'NIPA',
        'TableName': table_name,
        'Frequency': frequency,
        'Year': year
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.text()

    return data


def get_nipa_data(year):
    loop = asyncio.get_event_loop()
    nipa_table_args = []
    loop.run_until_complete(get_nipa_table_args(nipa_table_args))
    data = loop.run_until_complete(asyncio.gather(*(get_nipa_table_data(**args)
                                                    for args in nipa_table_args)))

    return data
