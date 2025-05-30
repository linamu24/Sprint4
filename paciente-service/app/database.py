from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://usuario:password@localhost/pacientesdb"
engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()