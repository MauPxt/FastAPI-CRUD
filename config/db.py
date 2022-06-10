from decouple import config
from sqlalchemy import create_engine, MetaData

engine = create_engine(
    f'mysql+pymysql://root:{config("dbpass")}@localhost:3306/fastapicrud')
meta = MetaData()
conn = engine.connect()
