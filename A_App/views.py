from django.shortcuts import render
import pymysql

# Create your views here.
def mysqlconect(sql):  ##数据库操作
    try:
        # 打开数据库连接
        # db = pymysql.connect("47.96.87.38", "chenzx", "123456", "eolinker_os");
        db = pymysql.connect("rm-bp146ki9wb74fp3o1uo.mysql.rds.aliyuncs.com", "finance_rd", "Rd$asd322", "finance_lease");

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        a = cursor.execute(sql)
        if sql.find("SELECT") >= 0:
            results = cursor.fetchall()
        else:
            results = a
        db.commit()
        # 关闭数据库连接
        db.close()
        return results
    except:
        # 如果发生错误则回滚
        db.rollback()


def List(request):
    sql = "SELECT b.id ,a.plate_number ,e.brand_name,c.idcard_name,c.idcard ,d.mobile ,e.contract_no_of_guotai ,e.contract_start_of_guotai ,e.contract_end_of_guotai ,e.msrp / 100 ,e.monthly_mortage_payment / 100,e.monthly_mortage_payment_day FROM trade_car_ready a,trade b,customer_info c,customer d,trade_info e WHERE a.trade_id = b.id AND b.customer_id = c.customer_id AND c.customer_id = d.id AND a.trade_id = e.trade_id"
    data = mysqlconect(sql)
    data_list = []
    titles = ['order_id', 'plate_number', 'brand_name', 'name', 'idcard', 'mobile', 'guotai_order', 'star_time',
              'end_time', 'msrp', 'monthly_mortage_payment', 'monthly_mortage_payment_day']
    nu = len(titles)
    for row in data:
        result = {}
        if (int(row[0]) > 50190213000041):
            for i in range(nu):
                result[titles[i]] = str(row[i]).replace('.0000','')
            data_list.append(result)
    data={
        "list":data_list
    }

    return render(request, 'list.html',data)

# if __name__ == '__main__':


