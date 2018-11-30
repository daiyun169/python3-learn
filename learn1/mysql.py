import MySQLdb
import random

# 打开数据库
# db = MySQLdb.connect("10.10.11.164", "test123", "test123", "rcm_db", charset='utf8')
db = MySQLdb.connect("10.10.8.205", "caocao", "caocao123", "rcm_db", charset='utf8')
# 获取游标
cur = db.cursor()


def repair1():
    brand_user_sql = "select * from brand_user"
    try:
        cur.execute(brand_user_sql)
        results = cur.fetchall()
        for row in results:
            id = row[0]
            brandName = str(row[10]).split(">")
            brandName.reverse()
            update_sql = "update brand_user set brand_type_name = '%s' where id = %d" % (">".join(brandName), id)
            print(update_sql)
            cur.execute(update_sql)
        db.commit()
    except:
        print('error: unable to fecth data')
    db.close()


# repair1()

def initUsers():
    # 查询品牌名称
    try:
        brandAreaSql = "select id, brand_name, brand_type, brand_type_name from brand_area"
        cur.execute(brandAreaSql)
        results = cur.fetchall()
        brandName = [row for row in results]
    except Exception as e:
        print("error: fetch brandarea")

    # 用户信息
    rangeHnUserIds = range(1000001, 1000010)

    for uid in rangeHnUserIds:
        try:
            # 品牌信息
            # print(brandName)
            brand = brandName[random.randint(0, len(brandName)) - 1]
            brandId = int(brand[0])
            brandType = int(brand[2])
            brandTypeNameAndBrandName = brand[3] + '>' + brand[1]
            userAccount = 'm' + str(uid)
            userName = 'name' + str(uid)
            sql1 = "INSERT INTO `rcm_db`.`brand_user` (`hn_user_id`, `brand_id`, `user_account`, `user_name`, `brand_type`, `brand_type_name`) VALUES " \
                   "('%d', '%d', '%s', '%s', '%d', '%s')" % (
                       uid, brandId, userAccount, userName, brandType, brandTypeNameAndBrandName)
            print(sql1)
            cur.execute(sql1)
            brandUserId = int(cur.lastrowid)
            print('brandUserId: ', brandUserId)

            sql2 = "INSERT INTO `rcm_db`.`brand_user_index` (`brand_user_id`, `hn_user_id`, `brand_id`, `goods_index`) VALUES ('%d', '%d', " \
                   "'%d', '%d')" % (
                       brandUserId, uid, brandId, random.randint(0, 10000))
            print(sql2)
            cur.execute(sql2)
            db.commit()
            print('success: ', uid)
        except:
            print('error db execute')
            db.rollback()


# initUsers()

import csv
import xlrd
import time


def read_csv(path):
    with open(path) as myFile:
        lines = csv.reader(myFile)
        # return [line for line in lines]
        return list(lines)


def read_excel(path):
    book = xlrd.open_workbook(path)
    sheet1 = book.sheet_by_index(0)
    # print('第一个工作簿名称：%s' % sheet1.name, '行数：%d' % sheet1.nrows, '列数：%d' % sheet1.ncols, sep='\t')
    brand_list = []
    for i in range(sheet1.nrows):
        if i == 0:
            continue
        brand_list.append(sheet1.row_values(i))
    return brand_list


def init_brand():
    sql = 'select brand_type, brand_type_name from brand_type'
    cur.execute(sql)
    results = cur.fetchall()
    brand_type_dict = {}
    for row in results:
        brand_type_dict[row[1]] = row[0]
    print(brand_type_dict)

    area = read_excel(r'C:\Users\qewli12\Desktop\area.xlsx')
    pd = {}
    cd = {}
    ad = {}
    for item in area:
        pd[item[0]] = item[1]
        cd[item[2]] = item[3]
        ad[item[4]] = item[5]

    install_brand_list = read_excel(r'C:\Users\qewli12\Desktop\中国好农货区域品牌资料表.xlsx')
    print(install_brand_list)

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(now)

    for brand_items in install_brand_list:
        brand_type_name = brand_items[0]
        brand_type = brand_type_dict.get(brand_type_name)
        brand_area_name = "%s/%s/%s" % (brand_items[2], brand_items[3], brand_items[4])
        if brand_type is None:
            print("\033[0;37;41m导入的数据有误，品类名称不在预设品类里面[%s]\033[0m" % brand_type)
        elif len(brand_items) != 7:
            print('\033[0;37;41m导入的数据有误，列数不正确\033[0m')
        else:
            # 数据正常开始插入
            try:
                pid = int(pd.get(brand_items[2]))
                cid = int(cd.get(brand_items[3]))
                aid = int(0 if brand_items[4] == '' is None else ( 0 if ad.get(brand_items[4]) is None else ad.get(brand_items[4])))
                # print(pid, cid, aid)
                brand_insert_sql = "INSERT INTO `rcm_db`.`brand_area` (`brand_name`, `brand_img`, `brand_desc`, `brand_type`, `brand_type_name`, `brand_area_name`, `province_id`, `city_id`, `area_id`, `opt_time`, `opt_name`) VALUES " \
                                   "( '%s', 'url', '%s', '%d', '%s', '%s', '%d', '%d', '%d', '%s', 'system')" % \
                                   (brand_items[1], brand_items[5], brand_type, brand_type_name, brand_area_name,
                                    pid, cid, int(aid), now)
                print(brand_insert_sql)

                cur.execute(brand_insert_sql)
                db.commit()
            except Exception as e:
                print('\033[0;37;41m区域品牌：%s  执行失败：%s \033[0m' % (brand_items[1], e))


# list = read_csv(r'C:\Users\qewli12\Desktop\中国好农货区域品牌资料表.csv')
# print(list)
#
# list2 = read_excel(r'C:\Users\qewli12\Desktop\中国好农货区域品牌资料表.xlsx')
# print(list2)

init_brand()

# area = read_excel(r'C:\Users\qewli12\Desktop\area.xlsx')
# pd = {}
# cd = {}
# ad = {}
# for item in area:
#     pd[item[1]] = item[0]
#     cd[item[3]] = item[2]
#     ad[item[5]] = item[4]
#
# print(pd.__len__())
# print(cd.__len__())
# print(ad.__len__())
