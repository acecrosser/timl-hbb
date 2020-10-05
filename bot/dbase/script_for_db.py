import psycopg2

connect = psycopg2.connect(dbname='timl_money',
                           user='timl',
                           password='OSXC715MICHElle',
                           host='localhost')

cursor = connect.cursor()
