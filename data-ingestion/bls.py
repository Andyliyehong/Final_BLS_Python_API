import datetime
from flask import Flask, request, redirect, url_for, flash, jsonify
import requests
import json
import math

registrationkey1 = "08580c73b25b4e61bf206ebded26af15"
registrationkey2 = "0310114879de4413ad6b6f8de6e7764c"
registrationkey3 = "a20abec182b94c8e968357e689df2917"

BASE_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"


def generate_df(startYear, endYear, seriesID_list, target_value_name, registrationkey):
    print(seriesID_list)

    if len(seriesID_list) > 20:
        n = math.ceil(len(seriesID_list) / 20)
        print("n equals to", n)
        i = 1
        new_seriesID_list = []
        year_list = []
        month_list = []
        target_value_list = []
        while i <= n:
            if i < n:
                sub_id_list = seriesID_list[(20 * (i - 1)):(20 * i)]
                print("sub_id_list equals to", sub_id_list)
                headers = {'Content-type': 'application/json'}
                data = json.dumps({"seriesid": sub_id_list, "startyear": startYear, "endyear": endYear,
                                   "registrationkey": registrationkey})
                p = requests.post(BASE_URL, data=data, headers=headers)
                print(p.text)
                if p.status_code == 200:
                    target_value = json.loads(p.text)
                    for item1 in target_value['Results']['series']:
                        seriesID = item1['seriesID']
                        for item2 in item1['data']:
                            year = item2['year']
                            month = item2['periodName']
                            target = item2['value']
                            new_seriesID_list.append(seriesID)
                            year_list.append(year)
                            month_list.append(month)
                            target_value_list.append(target)
                else:
                    return "Fail", p.status_code
            else:
                sub_id_list = seriesID_list[(20 * (i - 1)):]
                headers = {'Content-type': 'application/json'}
                data = json.dumps({"seriesid": sub_id_list, "startyear": startYear, "endyear": endYear,
                                   "registrationkey": registrationkey})
                p = requests.post(BASE_URL, data=data, headers=headers)
                print(p.text)
                if p.status_code == 200:
                    target_value = json.loads(p.text)
                    for item1 in target_value['Results']['series']:
                        seriesID = item1['seriesID']
                        for item2 in item1['data']:
                            year = item2['year']
                            month = item2['periodName']
                            target = item2['value']
                            new_seriesID_list.append(seriesID)
                            year_list.append(year)
                            month_list.append(month)
                            target_value_list.append(target)
                else:
                    return "Fail", p.status_code

            i = i + 1
        data = {'seriesID': new_seriesID_list,
                'year': year_list,
                'month': month_list,
                target_value_name: target_value_list
                }
        return data
    else:
        print("the length of seriesID list is less than 20")
        headers = {'Content-type': 'application/json'}
        data = json.dumps({"seriesid": seriesID_list, "startyear": startYear, "endyear": endYear,
                           "registrationkey": registrationkey})
        p = requests.post(BASE_URL, data=data, headers=headers)
        print(p.text)
        if p.status_code == 200:
            target_value = json.loads(p.text)
            seriesID_list = []
            year_list = []
            month_list = []
            target_value_list = []
            for item1 in target_value['Results']['series']:
                seriesID = item1['seriesID']
                for item2 in item1['data']:
                    year = item2['year']
                    month = item2['periodName']
                    target = item2['value']
                    seriesID_list.append(seriesID)
                    year_list.append(year)
                    month_list.append(month)
                    target_value_list.append(target)
            data = {'seriesID': seriesID_list,
                    'year': year_list,
                    'month': month_list,
                    target_value_name: target_value_list
                    }

            return data
        else:
            return "Fail", p.status_code


def get_ui_data(year):
    seriesID_list = ["LAUST010000000000006",
                     "LAUST020000000000006",
                     "LAUST040000000000006",
                     "LAUST050000000000006",
                     "LAUST060000000000006",
                     "LAUST080000000000006",
                     "LAUST090000000000006",
                     "LAUST100000000000006",
                     "LAUST110000000000006",
                     "LAUST120000000000006",
                     "LAUST130000000000006",
                     "LAUST150000000000006",
                     "LAUST160000000000006",
                     "LAUST170000000000006",
                     "LAUST180000000000006",
                     "LAUST190000000000006",
                     "LAUST200000000000006",
                     "LAUST210000000000006",
                     "LAUST220000000000006",
                     "LAUST230000000000006",
                     "LAUST240000000000006",
                     "LAUST250000000000006",
                     "LAUST260000000000006",
                     "LAUST270000000000006",
                     "LAUST280000000000006",
                     "LAUST290000000000006",
                     "LAUST300000000000006",
                     "LAUST310000000000006",
                     "LAUST320000000000006",
                     "LAUST330000000000006",
                     "LAUST340000000000006",
                     "LAUST350000000000006",
                     "LAUST360000000000006",
                     "LAUST370000000000006",
                     "LAUST380000000000006",
                     "LAUST390000000000006",
                     "LAUST400000000000006",
                     "LAUST410000000000006",
                     "LAUST420000000000006",
                     "LAUST440000000000006",
                     "LAUST450000000000006",
                     "LAUST460000000000006",
                     "LAUST470000000000006",
                     "LAUST480000000000006",
                     "LAUST490000000000006",
                     "LAUST500000000000006",
                     "LAUST510000000000006",
                     "LAUST530000000000006",
                     "LAUST540000000000006",
                     "LAUST550000000000006",
                     "LAUST560000000000006",
                     "LAUST010000000000005",
                     "LAUST020000000000005",
                     "LAUST040000000000005",
                     "LAUST050000000000005",
                     "LAUST060000000000005",
                     "LAUST080000000000005",
                     "LAUST090000000000005",
                     "LAUST100000000000005",
                     "LAUST110000000000005",
                     "LAUST120000000000005",
                     "LAUST130000000000005",
                     "LAUST150000000000005",
                     "LAUST160000000000005",
                     "LAUST170000000000005",
                     "LAUST180000000000005",
                     "LAUST190000000000005",
                     "LAUST200000000000005",
                     "LAUST210000000000005",
                     "LAUST220000000000005",
                     "LAUST230000000000005",
                     "LAUST240000000000005",
                     "LAUST250000000000005",
                     "LAUST260000000000005",
                     "LAUST270000000000005",
                     "LAUST280000000000005",
                     "LAUST290000000000005",
                     "LAUST300000000000005",
                     "LAUST310000000000005",
                     "LAUST320000000000005",
                     "LAUST330000000000005",
                     "LAUST340000000000005",
                     "LAUST350000000000005",
                     "LAUST360000000000005",
                     "LAUST370000000000005",
                     "LAUST380000000000005",
                     "LAUST390000000000005",
                     "LAUST400000000000005",
                     "LAUST410000000000005",
                     "LAUST420000000000005",
                     "LAUST440000000000005",
                     "LAUST450000000000005",
                     "LAUST460000000000005",
                     "LAUST470000000000005",
                     "LAUST480000000000005",
                     "LAUST490000000000005",
                     "LAUST500000000000005",
                     "LAUST510000000000005",
                     "LAUST530000000000005",
                     "LAUST540000000000005",
                     "LAUST550000000000005",
                     "LAUST560000000000005",
                     "LAUST010000000000004",
                     "LAUST020000000000004",
                     "LAUST040000000000004",
                     "LAUST050000000000004",
                     "LAUST060000000000004",
                     "LAUST080000000000004",
                     "LAUST090000000000004",
                     "LAUST100000000000004",
                     "LAUST110000000000004",
                     "LAUST120000000000004",
                     "LAUST130000000000004",
                     "LAUST150000000000004",
                     "LAUST160000000000004",
                     "LAUST170000000000004",
                     "LAUST180000000000004",
                     "LAUST190000000000004",
                     "LAUST200000000000004",
                     "LAUST210000000000004",
                     "LAUST220000000000004",
                     "LAUST230000000000004",
                     "LAUST240000000000004",
                     "LAUST250000000000004",
                     "LAUST260000000000004",
                     "LAUST270000000000004",
                     "LAUST280000000000004",
                     "LAUST290000000000004",
                     "LAUST300000000000004",
                     "LAUST310000000000004",
                     "LAUST320000000000004",
                     "LAUST330000000000004",
                     "LAUST340000000000004",
                     "LAUST350000000000004",
                     "LAUST360000000000004",
                     "LAUST370000000000004",
                     "LAUST380000000000004",
                     "LAUST390000000000004",
                     "LAUST400000000000004",
                     "LAUST410000000000004",
                     "LAUST420000000000004",
                     "LAUST440000000000004",
                     "LAUST450000000000004",
                     "LAUST460000000000004",
                     "LAUST470000000000004",
                     "LAUST480000000000004",
                     "LAUST490000000000004",
                     "LAUST500000000000004",
                     "LAUST510000000000004",
                     "LAUST530000000000004",
                     "LAUST540000000000004",
                     "LAUST550000000000004",
                     "LAUST560000000000004",
                     "LAUST010000000000003",
                     "LAUST020000000000003",
                     "LAUST040000000000003",
                     "LAUST050000000000003",
                     "LAUST060000000000003",
                     "LAUST080000000000003",
                     "LAUST090000000000003",
                     "LAUST100000000000003",
                     "LAUST110000000000003",
                     "LAUST120000000000003",
                     "LAUST130000000000003",
                     "LAUST150000000000003",
                     "LAUST160000000000003",
                     "LAUST170000000000003",
                     "LAUST180000000000003",
                     "LAUST190000000000003",
                     "LAUST200000000000003",
                     "LAUST210000000000003",
                     "LAUST220000000000003",
                     "LAUST230000000000003",
                     "LAUST240000000000003",
                     "LAUST250000000000003",
                     "LAUST260000000000003",
                     "LAUST270000000000003",
                     "LAUST280000000000003",
                     "LAUST290000000000003",
                     "LAUST300000000000003",
                     "LAUST310000000000003",
                     "LAUST320000000000003",
                     "LAUST330000000000003",
                     "LAUST340000000000003",
                     "LAUST350000000000003",
                     "LAUST360000000000003",
                     "LAUST370000000000003",
                     "LAUST380000000000003",
                     "LAUST390000000000003",
                     "LAUST400000000000003",
                     "LAUST410000000000003",
                     "LAUST420000000000003",
                     "LAUST440000000000003",
                     "LAUST450000000000003",
                     "LAUST460000000000003",
                     "LAUST470000000000003",
                     "LAUST480000000000003",
                     "LAUST490000000000003",
                     "LAUST500000000000003",
                     "LAUST510000000000003",
                     "LAUST530000000000003",
                     "LAUST540000000000003",
                     "LAUST550000000000003",
                     "LAUST560000000000003"]

    endYear = year
    startYear = endYear - 1
    lb_list = []
    uv_list = []
    ur_list = []
    ev_list = []
    for i in seriesID_list:
        if i[-2:] == "06":
            lb_list.append(i)
        if i[-2:] == "05":
            ev_list.append(i)
        if i[-2:] == "04":
            uv_list.append(i)
        if i[-2:] == "03":
            ur_list.append(i)

    state_dictionary = {'ST01': 'Alabama',
                        'ST02': 'Alaska',
                        'ST04': 'Arizona',
                        'ST05': 'Arkansas',
                        'ST06': 'California',
                        'ST08': 'Colorado',
                        'ST09': 'Connecticut',
                        'ST10': 'Delaware',
                        'ST11': 'District of Columbia',
                        'ST12': 'Florida',
                        'ST13': 'Georgia',
                        'ST15': 'Hawaii',
                        'ST16': 'Idaho',
                        'ST17': 'Illinois',
                        'ST18': 'Indiana',
                        'ST19': 'Iowa',
                        'ST20': 'Kansas',
                        'ST21': 'Kentucky',
                        'ST22': 'Louisiana',
                        'ST23': 'Maine',
                        'ST24': 'Maryland',
                        'ST25': 'Massachusetts',
                        'ST26': 'Michigan',
                        'ST27': 'Minnesota',
                        'ST28': 'Mississippi',
                        'ST29': 'Missouri',
                        'ST30': 'Montana',
                        'ST31': 'Nebraska',
                        'ST32': 'Nevada',
                        'ST33': 'New Hampshire',
                        'ST34': 'New Jersey',
                        'ST35': 'New Mexico',
                        'ST36': 'New York',
                        'ST37': 'North Carolina',
                        'ST38': 'North Dakota',
                        'ST39': 'Ohio',
                        'ST40': 'Oklahoma',
                        'ST41': 'Oregon',
                        'ST42': 'Pennsylvania',
                        'ST44': 'Rhode Island',
                        'ST45': 'South Carolina',
                        'ST46': 'South Dakota',
                        'ST47': 'Tennessee',
                        'ST48': 'Texas',
                        'ST49': 'Utah',
                        'ST50': 'Vermont',
                        'ST51': 'Virginia',
                        'ST53': 'Washington',
                        'ST54': 'Virginia',
                        'ST55': 'Wisconsin',
                        'ST56': 'Wyoming'}

    if len(lb_list) > 0:
        df_lb = generate_df(startYear, endYear, lb_list, "labor_force", registrationkey1)
        k = []
        for i in (list(map(lambda x: x[3:7], df_lb['seriesID']))):
            k.append(state_dictionary[i])
        df_lb['state'] = k

    elif len(lb_list) == 0:
        df_lb = {'seriesID': [],
                 'year': [],
                 'month': [],
                 'labor_force': [],
                 'state': []
                 }

    if len(uv_list) > 0:
        df_uv = generate_df(startYear, endYear, uv_list, "unemployment_value", registrationkey1)
        k = []
        for i in (list(map(lambda x: x[3:7], df_uv['seriesID']))):
            k.append(state_dictionary[i])
        df_uv['state'] = k
    elif len(uv_list) == 0:
        df_uv = {'seriesID': [],
                 'year': [],
                 'month': [],
                 'unemployment_value': [],
                 'state': []
                 }

    if len(ur_list) > 0:
        df_ur = generate_df(startYear, endYear, ur_list, "unemployment_rate", registrationkey1)
        k = []
        for i in (list(map(lambda x: x[3:7], df_ur['seriesID']))):
            k.append(state_dictionary[i])
        df_ur['state'] = k
    elif len(ur_list) == 0:
        df_ur = {'seriesID': [],
                 'year': [],
                 'month': [],
                 'unemployment_rate': [],
                 'state': []
                 }

    if len(ev_list) > 0:
        df_ev = generate_df(startYear, endYear, ev_list, "employment_value", registrationkey1)
        k = []
        for i in (list(map(lambda x: x[3:7], df_ev['seriesID']))):
            k.append(state_dictionary[i])
        df_ev['state'] = k
    elif len(ev_list) == 0:
        df_ev = {'seriesID': [],
                 'year': [],
                 'month': [],
                 'employment_value': [],
                 'state': []
                 }

    def custom_merge(unit1, unit2):
        out = {**unit1, **unit2}
        for key, value in out.items():
            if key in unit1 and key in unit2:
                out[key] = unit1[key]
        return out

    df_1 = custom_merge(custom_merge(custom_merge(df_lb, df_uv), df_ur), df_ev)

    df_unemployment_index = dict((k, df_1[k]) for k in ["state", "year", "month", "labor_force",
                                                        "employment_value", "unemployment_value", "unemployment_rate"]
                                 if k in df_1)

    df_unemployment = json.dumps(df_unemployment_index)
    print(df_unemployment)
    return df_unemployment, 200


def get_cpi_data(year):
    seriesID_list = ["CUUR0100SAS4",
                     "CUUR0100SAT",
                     "CUUR0100SAM",
                     "CUUR0100SAS2RS",
                     "CUUR0100SAF1",
                     "CUUR0100SAF114",
                     "CUUR0100SAF116",
                     "CUUR0200SAS4",
                     "CUUR0200SAT",
                     "CUUR0200SAM",
                     "CUUR0200SAS2RS",
                     "CUUR0200SAF1",
                     "CUUR0200SAF114",
                     "CUUR0200SAF116",
                     "CUUR0230SAT",
                     "CUUR0230SAM",
                     "CUUR0230SAF1",
                     "CUUR0230SAF114",
                     "CUUR0230SAF116",
                     "CUUR0240SAT",
                     "CUUR0240SAM",
                     "CUUR0240SAF1",
                     "CUUR0240SAF114",
                     "CUUR0240SAF116",
                     "CUUR0300SAS4",
                     "CUUR0300SAT",
                     "CUUR0300SAM",
                     "CUUR0300SAS2RS",
                     "CUUR0300SAF1",
                     "CUUR0300SAF114",
                     "CUUR0300SAF116",
                     "CUUR0360SAT",
                     "CUUR0360SAM",
                     "CUUR0360SAF1",
                     "CUUR0360SAF114",
                     "CUUR0360SAF116",
                     "CUUR0370SAT",
                     "CUUR0370SAM",
                     "CUUR0370SAF1",
                     "CUUR0370SAF114",
                     "CUUR0370SAF116",
                     "CUUR0400SAS4",
                     "CUUR0400SAT",
                     "CUUR0400SAM",
                     "CUUR0400SAS2RS",
                     "CUUR0400SAF1",
                     "CUUR0400SAF114",
                     "CUUR0400SAF116",
                     "CUUR0490SAT",
                     "CUUR0490SAM",
                     "CUUR0490SAF1",
                     "CUUR0490SAF114",
                     "CUUR0490SAF116"]

    endYear = year
    startYear = endYear - 1
    # SAS4	Transportation Services
    # SAT	Transportation
    # SAM	Medical care
    # SAS2RS 	Rent of shelter
    # SEMF 	Medicinal drugs
    # SAF1 	Food
    ## SAF113 	Fruits and vegetables
    # SAF114 	Nonalcoholic beverages and beverage materials
    # SAF116 	Alcoholic beverages

    ts_list = []
    t_list = []
    mc_list = []
    rs_list = []
    md_list = []
    f_list = []
    nab_list = []
    ab_list = []

    for i in seriesID_list:
        if i[8:] == "SAS4":
            ts_list.append(i)
        if i[8:] == "SAT":
            t_list.append(i)
        if i[8:] == "SAM":
            mc_list.append(i)
        if i[8:] == "SAS2RS":
            rs_list.append(i)
        if i[8:] == "SEMF":
            md_list.append(i)
        if i[8:] == "SAF1":
            f_list.append(i)
        if i[8:] == "SAF114":
            nab_list.append(i)
        if i[8:] == "SAF116":
            ab_list.append(i)

    area_dictionary = {'R0100': 'Northeast',
                       'R0200': 'Midwest',
                       'R0230': 'East North Central',
                       'R0240': 'West North Central',
                       'R0300': 'South',
                       'R0360': 'East South Central',
                       'R0370': 'West South Central',
                       'R0400': 'West',
                       'R0490': 'Pacific'}

    if len(ts_list) > 0:
        df_ts = generate_df(startYear, endYear, ts_list, "Transportation_Services", registrationkey2)
        k = []
        for i in (list(map(lambda x: x[3:8], df_ts['seriesID']))):
            k.append(area_dictionary[i])
        df_ts['area'] = k
    elif len(ts_list) == 0:
        df_ts = {'seriesID': [],
                 'year': [],
                 'month': [],
                 'Transportation_Services': [],
                 'area': []}

    if len(t_list) > 0:
        df_t = generate_df(startYear, endYear, t_list, "Transportation", registrationkey2)
        k = []
        for i in (list(map(lambda x: x[3:8], df_t['seriesID']))):
            k.append(area_dictionary[i])
        df_t['area'] = k
    elif len(t_list) == 0:
        df_t = {'seriesID': [],
                'year': [],
                'month': [],
                'Transportation': [],
                'area': []}

    if len(mc_list) > 0:
        df_mc = generate_df(startYear, endYear, mc_list, "Medical_care", registrationkey2)
        k = []
        for i in (list(map(lambda x: x[3:8], df_mc['seriesID']))):
            k.append(area_dictionary[i])
        df_mc['area'] = k
    elif len(mc_list) == 0:
        df_mc = {'seriesID': [],
                 'year': [],
                 'month': [],
                 'Medical_care': [],
                 'area': []}

    if len(rs_list) > 0:
        df_rs = generate_df(startYear, endYear, rs_list, "Rent_of_shelter", registrationkey2)
        k = []
        for i in (list(map(lambda x: x[3:8], df_rs['seriesID']))):
            k.append(area_dictionary[i])
        df_rs['area'] = k
    elif len(rs_list) == 0:
        df_rs = {'seriesID': [],
                 'year': [],
                 'month': [],
                 'Rent_of_shelter': [],
                 'area': []}

    if len(md_list) > 0:
        df_md = generate_df(startYear, endYear, md_list, "Medicinal_drugs", registrationkey2)
        k = []
        for i in (list(map(lambda x: x[3:8], df_md['seriesID']))):
            k.append(area_dictionary[i])
        df_md['area'] = k
    elif len(md_list) == 0:
        df_md = {'seriesID': [],
                 'year': [],
                 'month': [],
                 'Medicinal_drugs': [],
                 'area': []}

    if len(f_list) > 0:
        df_f = generate_df(startYear, endYear, f_list, "Food", registrationkey2)
        k = []
        for i in (list(map(lambda x: x[3:8], df_f['seriesID']))):
            k.append(area_dictionary[i])
        df_f['area'] = k
    elif len(f_list) == 0:
        df_f = {'seriesID': [],
                'year': [],
                'month': [],
                'Food': [],
                'area_code': []}

    if len(nab_list) > 0:
        df_nab = generate_df(startYear, endYear, nab_list, "Nonalcoholic_beverages_and_beverage_materials",
                             registrationkey2)
        k = []
        for i in (list(map(lambda x: x[3:8], df_nab['seriesID']))):
            k.append(area_dictionary[i])
        df_nab['area'] = k
    elif len(nab_list) == 0:
        df_nab = {'seriesID': [],
                  'year': [],
                  'month': [],
                  'Nonalcoholic_beverages_and_beverage_materials': [],
                  'area': []}

    if len(ab_list) > 0:
        df_ab = generate_df(startYear, endYear, ab_list, "Alcoholic_beverages", registrationkey2)
        k = []
        for i in (list(map(lambda x: x[3:8], df_ab['seriesID']))):
            k.append(area_dictionary[i])
        df_ab['area'] = k
    elif len(ab_list) == 0:
        df_ab = {'seriesID': [],
                 'year': [],
                 'month': [],
                 'Alcoholic_beverages': [],
                 'area': []}

    def custom_merge(unit1, unit2):
        # Merge dictionaries and add values of same keys
        out = {**unit1, **unit2}
        for key, value in out.items():
            if key in unit1 and key in unit2:
                out[key] = unit1[key]
        return out

    df_2 = custom_merge(custom_merge(
        custom_merge(custom_merge(custom_merge(custom_merge(custom_merge(df_ts, df_t), df_mc), df_rs), df_md), df_f),
        df_nab), df_ab)

    df_cpi_index = dict((k, df_2[k]) for k in ["area", "year", "month", "Transportation_Services",
                                               "Transportation", "Medical_care", "Rent_of_shelter", "Medicinal_drugs",
                                               "Food",
                                               "Nonalcoholic_beverages_and_beverage_materials", "Alcoholic_beverages"]
                        if k in df_2)

    df_cpi = json.dumps(df_cpi_index)
    # print(df_cpi)
    return df_cpi, 200


###raw json

def get_ppi_data(year):
    seriesID_list = ["PCU221122221122411",
                     "PCU221122221122412",
                     "PCU221122221122413",
                     "PCU221122221122414",
                     "PCU221122221122415",
                     "PCU221122221122416",
                     "PCU221122221122417",
                     "PCU221122221122418",
                     "PCU221122221122419",
                     "PCU221122221122421",
                     "PCU221122221122422",
                     "PCU221122221122423",
                     "PCU221122221122424",
                     "PCU221122221122425",
                     "PCU221122221122426",
                     "PCU221122221122427",
                     "PCU221122221122428",
                     "PCU221122221122429",
                     "PCU221122221122431",
                     "PCU221122221122432",
                     "PCU221122221122433",
                     "PCU221122221122434",
                     "PCU221122221122435",
                     "PCU221122221122436",
                     "PCU221122221122437",
                     "PCU221122221122438",
                     "PCU221122221122439",
                     "PCU2212102212101121",
                     "PCU2212102212101122",
                     "PCU2212102212101123",
                     "PCU2212102212101124",
                     "PCU2212102212101125",
                     "PCU2212102212101126",
                     "PCU2212102212101127",
                     "PCU2212102212101128",
                     "PCU2212102212101129",
                     "PCU2212102212101131",
                     "PCU2212102212101132",
                     "PCU2212102212101133",
                     "PCU2212102212101134",
                     "PCU2212102212101135",
                     "PCU2212102212101136",
                     "PCU2212102212101137",
                     "PCU2212102212101138",
                     "PCU2212102212101139",
                     "PCU2212102212101141",
                     "PCU2212102212101142",
                     "PCU2212102212101143",
                     "PCU2212102212101144",
                     "PCU2212102212101145",
                     "PCU2212102212101146",
                     "PCU2212102212101147",
                     "PCU2212102212101148",
                     "PCU2212102212101149"]
    endYear = year
    startYear = endYear - 1
    electric_list = []
    natural_gas_list = []
    for i in seriesID_list:
        if i[3:16] == "2211222211224":
            electric_list.append(i)
        if i[3:17] == "22121022121011":
            natural_gas_list.append(i)

    area_dictionary = {'1': 'New England',
                       '2': 'Middle Atlantic',
                       '3': 'East North Central',
                       '4': 'West North Central',
                       '5': 'South Atlantic',
                       '6': 'East South Central',
                       '7': 'West South Central',
                       '8': 'Mountain',
                       '9': 'Pacific'}
    elec_dic = {'1': 'residential', '2': 'commercial', '3': 'industrial', '': None}

    if len(electric_list) > 0:
        df_electric = generate_df(startYear, endYear, electric_list, "electric_power", registrationkey3)

        k = []
        for i in (list(map(lambda x: x[-1], df_electric['seriesID']))):
            k.append(area_dictionary[i])
        df_electric['area'] = k
        t = []
        for i in (list(map(lambda x: x[-2], df_electric['seriesID']))):
            t.append(elec_dic[i])
        df_electric['electric_power_type'] = t

    elif len(electric_list) == 0:
        df_electric = {'seriesID': [],
                       'year': [],
                       'month': [],
                       'electric_power': [],
                       'area': [],
                       'electric_power_type': []}

    natural_dic = {'2': 'residential', '3': 'commercial', '4': 'industrial', '': None}

    if len(natural_gas_list) > 0:
        df_natural_gas = generate_df(startYear, endYear, natural_gas_list, "natural_gas", registrationkey3)
        k = []
        for i in (list(map(lambda x: x[-1], df_natural_gas['seriesID']))):
            k.append(area_dictionary[i])
        df_natural_gas['area'] = k
        t = []
        for i in (list(map(lambda x: x[-2], df_natural_gas['seriesID']))):
            t.append(natural_dic[i])
        df_natural_gas['natural_gas_type'] = t

    elif len(natural_gas_list) == 0:
        df_natural_gas = {'seriesID': [],
                          'year': [],
                          'month': [],
                          'natural_gas': [],
                          'area': [],
                          'natural_gas_type': []}

    #####
    def custom_merge(unit1, unit2):
        # Merge dictionaries and add values of same keys
        out = {**unit1, **unit2}
        for key, value in out.items():
            if key in unit1 and key in unit2:
                out[key] = unit1[key]
        return out

    df_3 = custom_merge(df_electric, df_natural_gas)

    df_ppi_index = dict((k, df_3[k]) for k in ["area", "year", "month", "electric_power",
                                               "natural_gas", "electric_power_type", "natural_gas_type"] if k in df_3)

    df_ppi = json.dumps(df_ppi_index)
    #    print(df_ppi)
    return df_ppi, 200