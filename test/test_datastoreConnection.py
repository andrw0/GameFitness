## Required to have a sqlite db at the location used below before running the tests

def test_create_connection():
    conn = create_connection("C:\temp\db\gamefitness.db")
    assert(conn != null)

def test_create_invalidconnection():
    conn = create_connection("sjdfljasldj")
    assert(conn == null)


def test_select_all_users():
    conn = create_connection("c:\temp\db\gamefitness.db")
    assert(conn != null)
    assert(select_all_users(conn) == 10)
    
