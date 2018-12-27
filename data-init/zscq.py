import MySQLdb
import random
import csv
import xlrd
import time

# 打开数据库
db = MySQLdb.connect("10.10.8.205", "caocao", "caocao123", "rcm_db", charset='utf8')

# 获取游标
cur = db.cursor()


def read_excel(path):
    """ 读取商标 excel 文件 """
    book = xlrd.open_workbook(path)
    sheet1 = book.sheet_by_index(0)
    # print('第一个工作簿名称：%s' % sheet1.name, '行数：%d' % sheet1.nrows, '列数：%d' % sheet1.ncols, sep='\t')
    excel_row_list = []
    for i in range(sheet1.nrows):
        if i == 0:
            continue
        # cell = sheet1.cell_type(i,15)
        excel_row_list.append(tuple(sheet1.row_values(i)[1:]))
    return excel_row_list


def init_trade_mark(path):
    """ 初始化商标数据 """

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    insert_template_sql = "INSERT INTO `hn_president`.`cq_trade_mark` (`trade_mark_type`, `trade_mark_no`, `trade_mark_name`, `agency`, `apply_time`, `first_trial_time`, `register_time`, `expiration_time`, `applicant`, `applicant_address`, `approved_commodities_services`, `approved_commodities_service_groups`, `legal_state`, `urls`, `operator`, `create_time`, `note`, `update_time`, `deleted`) VALUES " \
                          "('%s', '%s', '%s', '%s', '%s 00:00:00', '%s 00:00:00', '%s 00:00:00', '%s 00:00:00', '%s', '%s', '%s', '%s', '%s', '', '%s', '%s', '%s', '" + now + "', b'0')"

    # 读取 excel 生成列表[(1,2,3),(4,5,6)]
    sql_list = read_excel(path)

    for sql in sql_list:
        exec_sql = insert_template_sql % sql
        print(exec_sql)
        cur.execute(exec_sql)

    db.commit()
    return

    # try:
    #     cur.executemany(insert_template_sql, sql_list)
    #     assert cur.rowcount == len(sql_list), 'cur rowcount error'
    #     db.commit()
    # except Exception as e:
    #     print("db execute error", e)
    #     db.rollback()
    # finally:
    #     cur.close()
    #     db.close()


init_trade_mark(r'C:\Users\qewli12\Desktop\商标查询结果列表 惠农20181026.xlsx')
