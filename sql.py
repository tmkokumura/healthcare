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
    SUM(value) AS value
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
GROUP BY
    data_type,
    source_name,
    end_date
ORDER BY
    data_type ASC,
    source_name ASC,
    end_date ASC;
'''

I_HEALTHCARE = '''
INSERT INTO healthcare (
    data_type,
    source_name,
    source_version,
    device,
    unit,
    creation_date,
    creation_time,
    start_date,
    start_time,
    end_date,
    end_time,
    value
 ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
'''
