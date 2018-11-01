# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify, make_response
from contextlib import closing
from datetime import datetime
import sqlite3
import conf
import sql
import logging
logging.basicConfig(level=conf.LOG_LEVEL, format=conf.LOG_FORMAT)

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """
    初期表示
    :return: index.html
    """
    logging.info('--- Start [index()] ---')
    # 表示データ取得
    rec_data_types = select(sql.S_DATA_TYPE)
    rec_source_names = select(sql.S_SOURCE_NAME)
    rec_start_end_date = select(sql.S_START_END_DATE)

    data_types = [x[0] for x in rec_data_types]
    source_names = [x[0] for x in rec_source_names]
    start_date = format_date(rec_start_end_date[0][0])
    end_date = format_date(rec_start_end_date[0][1])

    logging.info('--- End [index()] ---')

    # 画面表示
    return render_template('index.html', data_types=data_types, source_names=source_names,
                           start_date=start_date, end_date=end_date)


@app.route('/chart', methods=['GET'])
def chart():
    """
    表示ボタン押下時（ajax呼び出し想定）
    :return: チャートデータ
    """
    logging.info('--- Start [chart()] ---')

    # パラメータ
    data_type = request.args.get('data_type')
    source_name = request.args.get('source_name')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    logging.info('data_type: {}'.format(data_type))
    logging.info('source_name: {}'.format(source_name))
    logging.info('start_date: {}'.format(start_date))
    logging.info('end_date: {}'.format(end_date))

    # データ取得
    params = (data_type, source_name, start_date, end_date)
    records = select(sql.S_CHART_DATA, params)
    logging.info('records count: {}'.format(len(records)))

    if len(records) > 0:
        # チャートデータを整形
        data = build_chart_data(records)

        # レスポンスデータ
        res = {'result': 'OK', 'data': data}

    else:
        # レスポンスデータ
        res = {'result': 'データが存在しません。'}

    logging.info('--- End [chart()] ---')

    return make_response(jsonify(res))


# SELECT文発行
def select(sql_str, params=None):

    logging.info('Sql statement: {}'.format(sql_str))
    logging.info('params: {}'.format(params))

    with closing(sqlite3.connect(conf.DATABASE)) as conn:
        cur = conn.cursor()

        if params is None:
            cur.execute(sql_str)
        else:
            cur.execute(sql_str, params)

        return cur.fetchall()


# 日付フォーマット
def format_date(sql_date):
    return datetime.strftime(datetime.strptime(sql_date, conf.SQL_DATE_FORMAT), conf.HTML_DATE_FORMAT)


# チャートデータを整形
def build_chart_data(records):
    data_types = []
    source_names = []
    dates = []
    values = []
    prev_data_type = records[0][0]
    prev_source_name = records[0][1]

    for record in records:
        data_type = record[0]
        source_name = record[1]
        date = record[2]
        value = record[3]

        if source_name != prev_source_name:
            source_names.append({'source_name': prev_source_name, 'dates': dates, 'values': values})
            dates.clear()
            values.clear()

        if data_type != prev_data_type:
            data_types.append({'data_type': prev_data_type, 'source_names': source_names})
            source_names.clear()

        dates.append(date)
        values.append(value)

        prev_data_type = data_type
        prev_source_name = source_name

    source_names.append({'source_name': prev_source_name, 'dates': [dates], 'values': [values]})
    data_types.append({'data_type': data_type, 'source_names': source_names})

    return data_types


if __name__ == '__main__':
    app.run()
