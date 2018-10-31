# -*- coding: utf-8 -*-
from tqdm import tqdm
from datetime import datetime
import xml.etree.ElementTree as et
import sqlite3
import logging
log_fmt = '%(asctime)s %(levelname)s %(name)s :%(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_fmt)


''' Constants '''
INPUT_FILE = 'input/healthcare.xml'
DATABASE = 'healthcare.sqlite3'
SQL = 'INSERT INTO healthcare (data_type, source_name, source_version, device, unit, creation_date, start_date, \
end_date, value) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %z"

''' Main script '''
logging.info('--- Start [import_data.py] ---')

# データベース接続
conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

# ファイルの内容でtreeを初期化
tree = et.ElementTree(file=INPUT_FILE)

# treeのroot要素を取得
root = tree.getroot()

# record要素をすべて読み込む
count = 0
for record in tqdm(root.findall('.Record')):

    data_type = record.attrib.get('type')
    source_name = record.attrib.get('sourceName')
    source_version = record.attrib.get('sourceVersion')
    device = record.attrib.get('device')
    unit = record.attrib.get('unit')
    creation_date = record.attrib.get('creationDate')
    start_date = record.attrib.get('startDate')
    end_date = record.attrib.get('endDate')
    value = record.attrib.get('value')

    creation_date = datetime.strptime(creation_date, DATE_FORMAT)
    start_date = datetime.strptime(start_date, DATE_FORMAT)
    end_date = datetime.strptime(end_date, DATE_FORMAT)

    params = (data_type, source_name, source_version, device, unit, creation_date, start_date, end_date, value)
    cur.execute(SQL, params)

    count += 1

conn.commit()
conn.close()

logging.info('{} records were inserted.'.format(count))
logging.info('--- End [import_data.py] ---')
