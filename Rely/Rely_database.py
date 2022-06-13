import pymysql
from Rely.Rely_AnalysisCases_FromYaml import YamlHandle


class DoMysql:
    # 读取数据库信息
    def __init__(self):
        host = YamlHandle().get_data('Config_Database_info', 'host')  # 数据库的ip地址
        user = YamlHandle().get_data('Config_Database_info', 'user')  # 数据库的账号
        password = YamlHandle().get_data('Config_Database_info', 'password')  # 数据库的密码
        port = YamlHandle().get_data('Config_Database_info', 'port')  # mysql数据库的端口号
        database = YamlHandle().get_data('Config_Database_info', 'database')  # mysql数据库的Database
        self.mysql = pymysql.connect(host=host, password=password, user=user, port=port, database=database)
        self.cursor = self.mysql.cursor()

    def close_connect(self):
        self.cursor.close()
        self.mysql.close()

    def execute_sql_string(self, sqlstring, sanstran=False):
        """
        将 sqlString 作为 SQL 命令执行。
        将可选输入 `sansTran` 设置为 true, 则运行命令时关闭显式事务提交或回滚。
        """
        cur = None
        try:
            cur = self.cursor
            print('Executing : Execute SQL String  |  %s ' % sqlstring)
            cur.execute(sqlstring)
            if not sanstran:
                self.mysql.commit()
                return True
        finally:
            if cur:
                if not sanstran:
                    self.mysql.rollback()
