'''Main module for application

Attributes:
    APP (object): The core Flask application object
'''


import sys

from flask import Flask, jsonify

from app import bea, wb, bls


APP = Flask(__name__)


@APP.route('/')
def health_check():
    '''Sample health check
    '''
    return jsonify({'message': 'ok'})


@APP.route('/bea/<int:year>', methods=['GET'])
def get_bea_data(year):
    '''Check for updates for BEA data
    '''
    response = bea.get_nipa_data(year)
    return jsonify(response)


@APP.route('/wb/<int:year>', methods=['GET'])
def get_wb_data(year):
    '''Check for updates for World Bank data
    '''
    response = wb.get_ppp_data(year)
    return jsonify(response)


@APP.route('/bls/ppi/<int:year>', methods=['GET'])
def get_bls_ppi_data(year):
    '''Check for updates for BLS PPI data
    '''
    response = bls_pycharm.get_ppi_data(year)
    return response


@APP.route('/bls/cpi_py/<int:year>', methods=['GET'])
def get_bls_cpi_data(year):
    '''Check for updates for BLS CPI data
    '''
    response = bls_pycharm.get_cpi_data(year)
    return response


@APP.route('/bls/ui_py/<int:year>', methods=['GET'])
def get_bls_ui_data(year):
    '''Check for updates for BLS UI data
    '''
    response = bls_pycharm.get_ui_data(year)
    return response


def main():
    '''Main method for application
    '''
    APP.run(host='0.0.0.0')
    return 0


if __name__ == '__main__':
    sys.exit(main())
