# -*- coding: utf-8 -*-
import logging

# database name
DATABASE = 'healthcare.sqlite3'

# log settings
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s %(levelname)s %(name)s :%(message)s'

# format
INPUT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S %z'
SQL_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
HTML_DATE_FORMAT = '%Y-%m-%d'
