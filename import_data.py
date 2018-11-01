# -*- coding: utf-8 -*-
from tqdm import tqdm
from datetime import datetime
import xml.etree.ElementTree as et
import sqlite3
import conf
import logging
logging.basicConfig(level=conf.LOG_LEVEL, format=conf.LOG_FORMAT)


''' Constants '''
INPUT_FILE = 'input/healthcare.xml'
SQL = 'INSERT INTO healthcare (data_type, source_name, source_version, device, unit, creation_date, start_date, \
end_date, value) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'


''' Functions '''
def format_date(date_str):
    return datetime.strftime(datetime.strptime(date_str, conf.INPUT_DATE_FORMAT), conf.SQL_DATE_FORMAT)


''' Main script '''
if __name__ == '__main__':
    logging.info('--- Start [import_data.py] ---')

    # データベース接続
    conn = sqlite3.connect(conf.DATABASE)
    cur = conn.cursor()

    # ファイルの内容でtreeを初期化
    tree = et.ElementTree(file=INPUT_FILE)

    # treeのroot要素を取得
    root = tree.getroot()

    # record要素をすべて読み込む
    count = 0
    for record in tqdm(root.findall('.Record')):

        # xmlからデータを取得
        data_type = record.attrib.get('type')
        source_name = record.attrib.get('sourceName')
        source_version = record.attrib.get('sourceVersion')
        device = record.attrib.get('device')
        unit = record.attrib.get('unit')
        creation_date = record.attrib.get('creationDate')
        start_date = record.attrib.get('startDate')
        end_date = record.attrib.get('endDate')
        value = record.attrib.get('value')

        # 日付フォーマット
        creation_date = format_date(creation_date)
        start_date = format_date(start_date)
        end_date = format_date(end_date)

        params = (data_type, source_name, source_version, device, unit, creation_date, start_date, end_date, value)
        cur.execute(SQL, params)

        count += 1

    conn.commit()
    conn.close()

    logging.info('{} records were inserted.'.format(count))
    logging.info('--- End [import_data.py] ---')

