import streamlit as st
from db import GiamSatConn

def main():
    st.set_page_config(
        page_title="This is the dashboard of medial review system",
        page_icon="",
    )

    st.write("# Welcome to Dashboard System 👋")

    st.sidebar.success("Select a pages above")

    st.markdown(
        """
        This dashboard page using Streamlit which is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see our dashboard 
        """
    )

    """
    st.code('for i in range(8): foo()')

    gs_conn = GiamSatConn()
    gs_conn.open_connect()
    ora_conn = gs_conn.ora_con
    cur = ora_conn.cursor()
    cur.prepare('select * from report_sys.dm_nhombhyt')
    cur.execute(None)
    res = cur.fetchall()
    for r in res:
        st.write(r)
    cur.close()
    """
    

if __name__ == "__main__":
    main()
