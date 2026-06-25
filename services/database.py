from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///database.db",
    echo=False
)

metadata = MetaData()

holdings = Table(
    "holdings",
    metadata,

    Column("id", Integer, primary_key=True),

    Column("ticker", String),

    Column("shares", Float),

    Column("buy_price", Float),

    Column("currency", String)
)

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
