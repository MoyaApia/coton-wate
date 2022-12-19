import pymysql.cursors
# Connect to the database
CONNECTION = pymysql.connect(host='localhost',
                             user='cotonwate',
                             password='cotonwate',
                             db='cotonwatedb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)