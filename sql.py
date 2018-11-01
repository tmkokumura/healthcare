# -*- coding: utf-8 -*-

S_DATA_TYPE = '''
SELECT 
    DISTINCT data_type
FROM
    healthcare
ORDER BY
    data_type ASC;
'''

S_SOURCE_NAME = '''
SELECT 
    DISTINCT source_name
FROM
    healthcare
ORDER BY
    source_name ASC;
'''

S_START_END_DATE = '''
SELECT
    MIN(end_date),
    MAX(end_date)
FROM
    healthcare;
'''

S_CHART_DATA = '''
SELECT
    data_type,
    source_name,
    end_date AS date,
    value
FROM
    healthcare
WHERE
    data_type IN (?)
AND
    source_name IN (?)
AND
    end_date >= ?
AND
    end_date <= ?
ORDER BY
    data_type ASC,
    source_name ASC,
    end_date ASC;
'''
