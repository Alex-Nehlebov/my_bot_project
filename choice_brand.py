import sqlite3 as sq


def brand_huggies():

    with sq.connect('child_world_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_child_world WHERE brand_name == 'Huggies' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_pampers():

    with sq.connect('child_world_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_child_world WHERE brand_name == 'Pampers' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_yokosun():

    with sq.connect('child_world_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_child_world WHERE brand_name == 'YokoSun' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_manu():

    with sq.connect('child_world_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_child_world WHERE brand_name == 'MANU' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def all_brand_regular():

    with sq.connect('child_world_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_child_world ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_yokosun_pants():

    with sq.connect('child_world_pants.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diaper_pants_child_world WHERE brand_name == 'YokoSun' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_huggies_pants():

    with sq.connect('child_world_pants.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diaper_pants_child_world WHERE brand_name == 'Huggies' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_pampers_pants():

    with sq.connect('child_world_pants.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diaper_pants_child_world WHERE brand_name == 'Pampers' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_manu_pants():

    with sq.connect('child_world_pants.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diaper_pants_child_world WHERE brand_name == 'MANU' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def all_brand_pants():

    with sq.connect('child_world_pants.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_child_world ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_huggies_stork():

    with sq.connect('stork_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_stork WHERE brand_name == 'Huggies ' OR brand_name == 'Huggies' 
            ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_yokosun_stork():

    with sq.connect('stork_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_stork WHERE brand_name == 'YokoSun' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_pampers_stork():

    with sq.connect('stork_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_stork WHERE brand_name == 'Pampers' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_watashi_stork():

    with sq.connect('stork_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_stork WHERE brand_name == 'WATASHI' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def all_brand_stork():

    with sq.connect('stork_diapers.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_stork ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_yokosun_all():

    with sq.connect('all.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_all WHERE brand_name == 'YokoSun' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_huggies_all():

    with sq.connect('all.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_all WHERE brand_name == 'Huggies ' OR brand_name == 'Huggies' 
            ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_pampers_all():

    with sq.connect('all.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_all WHERE brand_name == 'Pampers' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def brand_watashi_all():

    with sq.connect('all.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_all WHERE brand_name == 'WATASHI' ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result


def general_brand_all():

    with sq.connect('all.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT * FROM diapers_all ORDER BY actual_price ASC""")
        result = cur.fetchall()
        return result
