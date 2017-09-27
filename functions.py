def sqlite_connnect(reference_file):
    import json
    import sqlite3

    global connection
    global cursor

    with open(reference_file) as db:
        data = json.load(db)

    db_file = data['db_file']
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()


def sqlite_close():
    cursor.close()
    connection.commit()
    connection.close()


def sqlite_create_table(reference_file='db_schema.json', db_instance='tracer'):
    import json

    with open(reference_file) as db:
        data = json.load(db)

    if db_instance == '':
        db_instance = data['db_instance'][0]

    table_schema = data['table_schema'][db_instance]

    result = ""
    for key in table_schema:
        component = ("{} {}, ".format(key, table_schema[key]))
        result = result + component
    table_schema = result[:-2]

    create_table = "CREATE TABLE IF NOT EXISTS {}({})".format(db_instance, table_schema)
    cursor.execute(create_table)


def sqlite_insert_data(reference_file='/git/Tracer/db_schema.json', db_instance='tracer', values=''):
    import json

    with open(reference_file) as db:
        data = json.load(db)

    if db_instance == '':
        db_instance = data['db_instance'][0]

    cursor.execute("INSERT INTO {} VALUES ({})".format(db_instance, values))


def sqlite_query_all(table):
    cursor.execute("SELECT * FROM {}".format(table))
    values = cursor.fetchall()
    return values


def sqlite_query(query):
    cursor.execute("{}".format(query))
    values = cursor.fetchall()
    return values


def main(server='8.8.8.8', protocol='icmp', port='', count='3', output_path='./mtr-output.log'):
    import json
    from getpass import getuser
    import subprocess
    # mtr 8.8.8.8 -rwz -c 3 -o "SRDL ABW MX"
    # base_mtr_command = 'sudo mtr ' + server + ' -rwz -c ' + count + ' -o "SRDL ABW MX" --json > ' + output_path

    if getuser() == 'root':
        exec_mtr = 'mtr '
    else:
        exec_mtr = 'sudo mtr '

    mtr_command = exec_mtr + server + ' -nrwz -c ' + count + ' -o "SRDL ABW MX" --json'

    if protocol == 'icmp':
        newprocess = subprocess.getoutput(mtr_command)
        data = json.loads(newprocess)
        return data
    '''
    if protocol == 'tcp':
        base_mtr_command += "--tcp "
    elif protocol == 'ucp':
        base_mtr_command += "-udp "

    if protocol != 'icmp' and (0 < port <= 65535):
        base_mtr_command += "-P " + str(port) + " "
    '''


