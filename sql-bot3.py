import pymysql
import sys
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser

home = expanduser('~')
mypkey = paramiko.RSAKey.from_private_key_file(home + '/oscar-cloudops.pem')
# if you want to use ssh password use - ssh_password='your ssh password', bellow

sql_hostname = 'database-1.cws2nhzaqpvu.us-east-1.rds.amazonaws.com'
sql_username = 'admin'
sql_password = 'Tu998DR*h&3K^^0'
sql_main_database = 'mysql'
sql_port = 3306
ssh_host = '52.204.106.95'
ssh_user = 'ubuntu'
ssh_port = 22
sql_ip = '1.1.1.1.1'

print (sys.argv[1])
with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=mypkey,
        remote_bind_address=(sql_hostname, sql_port)) as tunnel:
    conn = pymysql.connect(host='127.0.0.1', user=sql_username,
            passwd=sql_password, 
            db=sql_main_database,
            port=tunnel.local_bind_port)
    query = '''SELECT user FROM user;'''
    data = pd.read_sql_query(query, conn)
    print(data)
    conn.close()