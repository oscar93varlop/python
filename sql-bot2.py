from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
     ('52.204.106.95', 22),
#     ssh_password="123ABC123",
     ssh_username="ubuntu",
     ssh_private_key=r'/home/oscarv/oscar-cloudops.pem',
     remote_bind_address=('127.0.0.1', 3306)
)

server.start()

engine = create_engine(
    f'mysql+database-1.cws2nhzaqpvu.us-east-1.rds.amazonaws.com://admin:Tu998DR*h&3K^^0@127.0.0.1:3306'
)
dbs = engine.execute('SHOW DATABASES;')
for db in dbs:
    print(db)

server.stop()