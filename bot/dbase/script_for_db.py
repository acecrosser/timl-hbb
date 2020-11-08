import psycopg2

connect = psycopg2.connect(dbname='timl_money',
                           user='bot_v02',
                           password='OSXC715MICHElle',
                           host='localhost')

cursor = connect.cursor()
