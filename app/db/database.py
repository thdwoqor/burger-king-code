import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# https://www.phpschool.com/gnuboard4/bbs/board.php?bo_table=qna_db&wr_id=132640

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))
load_dotenv()


DATABASE = f'mariadb+pymysql://{os.getenv("MARIADB_USER")}:{os.getenv("MARIADB_PASSWORD")}@{os.getenv("MARIADB_HOST")}:{os.getenv("MARIADB_PORT")}/{os.getenv("MARIADB_DATABASE")}?charset=utf8'


ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()
