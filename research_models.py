from sqlalchemy import (create_engine, Table, Column, Integer, String, Date, ForeignKey, Float, Boolean)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///research.db')


# Change att duration and funding_contract
class FundingSource(Base):
    __tablename__ = 'funding_sources'
    funding_id = Column('funding_id', Integer, autoincrement=True, primary_key=True)
    funding_source = Column('funding_source', String())
    funding_agency = Column('funding_agency', String())


class Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column('staff_id', Integer, autoincrement=True, primary_key=True)
    staff_firstname = Column('staff_firstname', String())
    staff_lastname = Column('staff_lastname', String())
    staff_email = Column('staff_email', String())
    work_position = Column ('work_position', String())
    academic_position = Column ('academic_positopn', String())
    startdate = Column('startdate', Date())
    graduate_degree = Column('graduate_degree', String())
    graduate_country = Column('graduate_country', String())



class Department(Base):
    __tablename__ = 'department'
    department_id = Column('department_id', Integer, autoincrement=True, primary_key=True)
    department_name = Column('department_name', String())

class Research(Base):
    __tablename__ = 'research'
    research_id = Column('research_id', Integer, autoincrement=True, primary_key=True)
    research_title_th = Column('research_title_th', String(200))
    research_title_en = Column('research_title_en', String(200))
    est_funding = Column('est_funding',Float())
    research_startdate = Column('research_startdate', Date())
    research_enddate = Column('research_enddate', Date())
    research_contract = Column('research_contract', Boolean())

class Date(Base):
    __tablename__ = 'date'
    date_id = Column('date_id', Integer, autoincrement=True, primary_key=True)
    date = Column('date', Date())
    calendar_month = Column('calendar_month', String(3))
    calendar_year = Column('calendar_year', Integer())
    fiscal_year_month = Column('fiscal_year_month', String(8))
    fiscal_quarter = Column('fiscal_quarter', String(2))
    academic_year = Column('academic_year', Integer())


class FundingResearchFact(Base):
    __tablename__ = 'funding_research_fact'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    funding_id = Column('funding_id', ForeignKey('funding_sources.funding_id'))
    research_id = Column('research_id', ForeignKey('research.research_id'))
    staff_id = Column('staff_id', ForeignKey('staff.staff_id'))
    department_id = Column('department_id', ForeignKey('department.department_id'))
    date_id = Column('date_id', ForeignKey('date.date_id'))
    publication_id = Column('publication_id', ForeignKey('publication.id'))
    journal_id = Column('journal_id', ForeignKey('journal.id'))
    citation_id = Column('citation_id', ForeignKey('citation.id'))
    each_funding = Column('total_funding', Float())

class publication(Base):
    __tablename__ = 'publication'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    title = Column('title', String())
    abstract = Column('abstract', String())
    publication_date = Column('publication_date', Date())

class journal(Base):
    __tablename__ = 'journal'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String())

class citation(Base):
    __tablename__ = 'citation'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    publication_id = Column('publication_id', ForeignKey('publication.id'))
    citation_count = Column('citation_count', Integer())
    last_update_date = Column('last_update_date', ForeignKey('Date.date_id'))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
