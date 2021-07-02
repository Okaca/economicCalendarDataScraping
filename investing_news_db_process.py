from sqlalchemy.sql.sqltypes import DateTime, Float
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine('postgresql+psycopg2://postgres:asd123@localhost:5432/postgres')
Base = declarative_base()

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise
    finally:
        session.close()


class InvestingNewsData(Base):
    __tablename__='InvestingNewsData'
    id = Column(Integer,primary_key = True,unique=True,autoincrement=True)
    event_time_clock = Column(String)
    country_name = Column(String)
    event_name = Column(String)
    volatility = Column(String)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

def addInvestingNewsData(event_time_clock, country_name, event_name, volatility):
    with session_scope() as s:
        std=InvestingNewsData(
            event_time_clock=event_time_clock,
            country_name=country_name,
            event_name=event_name,
            volatility=volatility
        )
        s.add(std)

def getInvestingNewsData():
    with session_scope() as s:
        news_list = s.query(InvestingNewsData).all()
        
        for elem in news_list:
            print(elem.event_time_clock, elem.country_name, elem.event_name, elem.volatility)