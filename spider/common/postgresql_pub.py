# coding:utf-8
import psycopg2
from config import read_config

def postgresql_select(sql):

    conn = psycopg2.connect(host=read_config.get_postgresl_info('host'), port=read_config.get_postgresl_info('port'), database=read_config.get_postgresl_info('database'), user=read_config.get_postgresl_info('user'), password=read_config.get_postgresl_info('password'))
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()        # all rows in table
    # print(rows)
    # for i in rows:
    #     print(i)
    conn.commit()
    conn.close()
    return rows

if __name__ == '__main__':
    sql = r'SELECT * from t_device_app'
    res = postgresql_select(sql)
    print(res[0])
    print(type(res[0]))