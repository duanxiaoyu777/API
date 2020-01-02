# coding=utf-8

import pymysql
from config.basic_config import ConfigInit
from loguru import logger


class MysqlDatabase:
    def __init__(self):
        self.db = self.connect_sql()

    def connect_sql(self):
        # 建立数据库连接
        con = pymysql.connect(host=ConfigInit.mysql_host, port=ConfigInit.mysql_port, user=ConfigInit.mysql_user,
                              password=ConfigInit.mysql_pw, db=ConfigInit.mysql_db, charset='utf8mb4')
        # con.autocommit(False)
        try:
            print('数据库连接成功')
        except Exception as e:
            print('连接数据库失败')
        return con

    def delete_individual_user(self):
        '''删除个人用户'''
        con = self.db
        cursor = con.cursor()       # 使用cursor()方法获取操作游标
        sql = " DELETE FROM member WHERE member_phone = '13800138915' "
        try:
            print("删除个人用户SQL执行中")
            cursor.execute(sql)     # 使用 execute()方法执行 SQL
            con.commit()            # 事务提交
            print('成功删除', cursor.rowcount, '条数据')
        except Exception as e:
            cursor.rollback()       # 如果发生错误则回滚
            print('事务处理失败', e)
        con.close()                 # 关闭数据库连接
        cursor.close()

    def delete_enterprise_user(self):
        '''删除企业用户'''
        con = self.db
        cursor = con.cursor()
        sql = " DELETE FROM member WHERE member_phone = '13800138916' "
        try:
            print("删除企业用户SQL执行中")
            cursor.execute(sql)
            con.commit()
            print('成功删除', cursor.rowcount, '条数据')
        except Exception as e:
            cursor.rollback()
            print('事务处理失败', e)
        con.close()
        cursor.close()

    def delete_order_partner(self):
        '''删除超时订单'''
        con = self.db
        cursor = con.cursor()
        sql = " DELETE FROM order_summary WHERE member_id = '419164672567152640' AND order_status = '5' AND order_bearing_state = '105' "
        try:
            print("删除超时订单SQL执行中")
            cursor.execute(sql)
            con.commit()
            print('成功删除', cursor.rowcount, '条数据')
        except Exception as e:
            cursor.rollback()
            print('事务处理失败', e)
        con.close()
        cursor.close()

    def Update_invoice_status(self):
        '''修改申请开票状态'''
        con = self.db
        cursor = con.cursor()
        sql = " UPDATE invoice_info_new SET admin_status = '4' WHERE invoice_title = '段小雨' "
        try:
            print("修改发票状态SQL执行中")
            cursor.execute(sql)
            con.commit()
            print('更新成功', cursor.rowcount, '条数据')
        except Exception as e:
            cursor.rollback()
            print('事务处理失败', e)
        con.close()
        cursor.close()

    def Update_confirm_money(self):
        '''更新认款状态'''
        con = self.db
        cursor = con.cursor()
        sql_1 = " UPDATE bank_running_water SET confirm_user_id = '' WHERE id = '843' "
        sql_2 = " DELETE FROM confirm_money_record WHERE bank_running_no = '2019101900236191550000000' "
        sql_3 = " DELETE FROM confirm_money_detail WHERE bank_running_no = '2019101900236191550000000' "
        sql_4 = " UPDATE order_summary SET confirm_fee = 0 WHERE order_id = '157758890275' "
        sql_5 = " UPDATE order_summary SET private_confirm_fee = 0 WHERE order_id = '157758890275' "

        try:
            print("更新认款状态SQL执行中")
            cursor.execute(sql_1)
            con.commit()
            print('更新成功', cursor.rowcount, '条数据')
            cursor.execute(sql_2)
            con.commit()
            print('删除成功', cursor.rowcount, '条数据')
            cursor.execute(sql_3)
            con.commit()
            print('删除成功', cursor.rowcount, '条数据')
            cursor.execute(sql_4)
            con.commit()
            print('更新成功', cursor.rowcount, '条数据')
            cursor.execute(sql_5)
            con.commit()
            print('更新成功', cursor.rowcount, '条数据')
        except Exception as e:
            cursor.rollback()
            print('事务处理失败', e)
        con.close()
        cursor.close()


# if __name__ == '__main__':
    # MysqlDatabase().delete_individual_user()
    # MysqlDatabase().delete_enterprise_user()
    # MysqlDatabase().Update_confirm_money()