import cx_Oracle
# import os
class OracleConnect:
    def __init__(self, ip, port, service_name, user_name, password):
        self.ip = ip
        self.port = port
        self.service_name = service_name
        self.user_name = user_name
        self.password = password

    def open_connect(self):
        # os.environ["NLS_LANG"] = "American_America.UTF8"
        dsn_tns = cx_Oracle.makedsn(self.ip, self.port, service_name = self.service_name)
        self.ora_con = cx_Oracle.connect(self.user_name, self.password, dsn_tns, encoding = 'utf-8', nencoding='utf-8')

    def close_connect(self):
        if self.ora_con:
            self.ora_con.close()

class GiamSatConn(OracleConnect):
    ip = '10.0.109.95'
    port = 1521
    service_name = 'GSGD'
    user_name = 'HUNGTT'
    password = 'poistra291'

    def __init__(self):
        OracleConnect.__init__(self, ip = GiamSatConn.ip, port =
                GiamSatConn.port, service_name = GiamSatConn.service_name, user_name = GiamSatConn.user_name, password = GiamSatConn.password)

    def __enter__(self):
        self.open_connect()
        return self.ora_con

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.close_connect()
        a = 1