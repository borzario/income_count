from sqlalchemy import create_engine



DIALECT     = 'postgresql'
DRIVER      = 'psycopg2'
USERNAME    = "user"
PASSWORD    = "user"
HOST        = "localhost"
PORT        = "5435"
DATABASE    = "avito"


ENGINE_STRING = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(ENGINE_STRING)
