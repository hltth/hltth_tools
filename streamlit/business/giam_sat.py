from db import GiamSatConn

class GiamSat:
    def __init__(self) -> None:
        # Init database connection
        self.__gs_conn = GiamSatConn()
        self.__gs_conn.open_connect()
        pass

    def __del__(self):
        self.__gs_conn.close_connect()
        print("Destructor called")    
        
    def load_thong_ke_chi_phi(self):
        ora_conn = self.__gs_conn.ora_con
        cur = ora_conn.cursor()
        cur.prepare("""
        select * 
          from report_sys.z_hung_tongchi 
         where ky_qt <= '2022-10-01'
          order by ky_qt
        """)
        cur.execute(None)
        res = cur.fetchall()
        cur.close()
        return res