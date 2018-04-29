import csv
import os
import random

import ujson as json

NUM_KEYS = [
    'a11_bsag_total', 'a11_bsag_anxiety', 'a11_bsag_depression', 'a23_pdistress', 
    'a33_pdistress', 'a42_pdistress'
]
STR_KEYS = [
    'cntrl_gender', 'cntrl_a11_social_class'
]

CLASS = {
    'I': 'Professional',
    'II': 'Managerial',
    'III non manu': 'Skilled non-manual',
    'III manual': 'Skilled manual',
    'IV': 'Partly skilled',
    'V': 'Unskilled',
}

GENDER = {'0': 'M', '1': 'F'}


def read_data(prefix):
    """ Takes the directory prefix. Returns merged data. """
    subjects = {}
    with open(f"{prefix}_variables.csv") as f:
        for row in csv.DictReader(f):
            id = row.pop('clp18_id')
            data = {}
            for k in NUM_KEYS:
                if k in row:
                    v = row[k].strip()
                    if v:
                        v = int(v.split('.')[0])
                    else:
                        v = ''
                    data[k] = v
            data.update({k: row[k] for k in STR_KEYS})
            data['cntrl_a11_social_class'] = CLASS[data['cntrl_a11_social_class']]
            data['cntrl_gender'] = GENDER[data['cntrl_gender']]
            data['id'] = id
            subjects[id] = data
    with open(f'{prefix}_a11essays.csv') as f:
        for row in csv.DictReader(f):
            subjects[row['clp18_id']]['essay'] = row['essay'].replace(r'\n', '\n')
    return subjects


def split_train_dev(subjects):
    keys = list(subjects.keys())
    random.seed(1)
    random.shuffle(keys)
    dev_keys = keys[-1000:]
    keys = keys[:-1000]
    train = {k: subjects[k] for k in keys}
    dev = {k: subjects[k] for k in dev_keys}
    return train, dev


def write_data(data, fname):
    with open(fname, 'w') as f:
        for id, data in data.items():
            data['id'] = id
            f.write(json.dumps(data) + '\n')


def load_jsonl(fname):
    data = []
    with open(fname) as f:
        return [json.loads(l.strip()) for l in f]
