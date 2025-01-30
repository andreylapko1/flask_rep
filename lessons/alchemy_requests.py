from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from dotenv import load_dotenv
import os
load_dotenv()

engine = create_engine(f'{os.getenv("str_read")}world')



Base = automap_base()
Base.prepare(engine, reflect=True)
Session = sessionmaker(bind=engine)



World = Base.classes.country



with Session() as session:
    employees = session.query(World).having(World.SurfaceArea > 5000000).all()
    for a in employees:
        print(a.Name + ':', a.SurfaceArea)









