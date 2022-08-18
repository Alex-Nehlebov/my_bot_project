import sqlite3 as sq


def add_info(params):

    with sq.connect('all.db') as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS diapers_all(
            name_id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand_name TEXT,
            name TEXT,
            size INTEGER,
            actual_price REAL,
            old_price REAL,
            store_name TEXT
            )""")
        cur.execute(
            f"""INSERT INTO diapers_all (brand_name, name, size, actual_price, old_price, store_name)
            VALUES(?, ?, ?, ?, ?, ?)""", params)


def create_general_bd():

    with sq.connect('stork_diapers.db') as con_stork:
        cur_stork = con_stork.cursor()
        cur_stork.execute("SELECT * FROM diapers_stork")
        result_stork = cur_stork.fetchall()
        for i_stork in result_stork:
            line_stork = i_stork[1:7]

            add_info(line_stork)

    with sq.connect('child_world_pants.db') as con_child:
        cur_child = con_child.cursor()
        cur_child.execute("SELECT * FROM diaper_pants_child_world")
        result_child = cur_child.fetchall()
        for i_child in result_child:
            line_child = i_child[1:7]

            add_info(line_child)

    with sq.connect('child_world_diapers.db') as con_child_2:
        cur_child_2 = con_child_2.cursor()
        cur_child_2.execute("SELECT * FROM diapers_child_world")
        result_child_2 = cur_child_2.fetchall()
        for i_child_2 in result_child_2:
            line_child_2 = i_child_2[1:7]

            add_info(line_child_2)


create_general_bd()
