from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer,ForeignKey
from sqlalchemy.orm import sessionmaker, declartive_base, relationship

Base = declartive_base()