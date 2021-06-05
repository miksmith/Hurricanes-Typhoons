from sqlalchemy import Column, String, Integer, Date, Time, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cyclone(Base):
    __tablename__ = 'cyclone'
    cyclone_id = Column(String, primary_key=True)
    cyclone_name = Column(String)
    region = Column(String)


class Measurements(Base):
    __tablename__ = 'measurements'
    status_id = Column(Integer, primary_key=True)
    cyclone_id = Column(Integer, ForeignKey('cyclone.cyclone_id'))
    measure_date = Column(Date)
    measure_time = Column(Time)
    event = Column(String)
    status = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    max_wind = Column(Integer)
    min_pressure = Column(Float)
    low_wind_ne = Column(Float)
    low_wind_se = Column(Float)
    low_wind_sw = Column(Float)
    low_wind_nw = Column(Float)
    mod_wind_ne = Column(Float)
    mod_wind_se = Column(Float)
    mod_wind_sw = Column(Float)
    mod_wind_nw = Column(Float)
    high_wind_ne = Column(Float)
    high_wind_se = Column(Float)
    high_wind_sw = Column(Float)
    high_wind_nw = Column(Float)
