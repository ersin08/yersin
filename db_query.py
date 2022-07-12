# Запросы в SQL

create_1 = '''create table Departments_db(
                    department_id int,
                    department_name varchar(30),
                    location_id int
                );
            '''

create_2 = '''create table employees (
    employee_id int,
    first_name varchar(30),
    last_name varchar(30),
    email varchar(30),
    phone_number BIGINT,
    hire_date varchar(30),
    job_id int,
    salary varchar(20),
    department_id int
    );
''' 

create_3 = '''create table jobs_db (
    job_id int,
    job_title varchar(20)
    );
'''

create_4 = '''create table location(
    loc_id int,
    street_address varchar(32),
    postal_code int,
    city varchar(32),
    country_id int
    );
'''

create_5 = '''create table countries (
    country_id int,
    country_name varchar(15)
    );
'''

insert_dep = '''insert into Departments_db(department_id, department_name, location_id) 
    values(1, 'Administration',120),
    (2, 'Marketing', 121),
    (3, 'Programmers', 122),
    (4, 'Sales managers',123),
    (5,'Shipping',1500),
    (6,'IT',1400),
    (7,'Public Relations',2700),
    (8,'Sales',2500),
    (9,'Executive',1700),
    (11,'Accounting',1700);
'''

insert_emp =   '''insert into employees(employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, department_id)
                    values(1,'Yersin','Konys','yersinkonys@gamil.com',87081288641,'2001-04-15',4, '240000.00',NULL),
                    (2,'Bekpenbet', 'Bolat','Bolat_tt@gamil.com', 8708118646,'2001-04-15',5, '260000.00',NULL),
                    (3, 'Yerek', 'Yerkinbekuly', 'yerkinbeluly@aues.kz', 8707118646, '1999-04-15',5, '260000.00',NULL),
                    (4, 'Raimbek', 'Adilkanov', 'raimkz@mail.ru', 8701222225, '2022-09-15', 5, '360000.00',NULL),
                    (5, 'Asu', 'Samatov', 'samatov@mail.ru', 87775552265, '2022-12-15',6, '870000.00',NULL),
                    (6, 'Aues', 'Aramanov', 'Bolatov@mail.ru', 8701222232, '2022-01-15',5, '160000.00',NULL);
            '''

insert_job = '''insert into jobs_db(job_id, job_title)
           values (11,' Accountant'),
           (8,'Sales Manager'),
           (3,'Programmer'), 
           (5,'Shipping Clerk'), 
           (6, 'Administration' );
          '''

insert_count = '''insert into countries(country_id, country_name) 
    values(1, 'Kazakhstan'),
          (10, 'Russia'),
          (2, 'United States'),
          (8, 'Uzbekistan');
        '''

insert_location = '''insert into location(loc_id, street_address, postal_code, city, country_id)
    values(400, '2014 Jabberwocky Rd', 26192,'Texas', 2),
          (401, 'K Azerabaev', 216192, 'Tashkent', 8),
          (401, 'Satbaev', 234234, 'Almaty', 1);
    '''    

task_2 = '''Select * from employee
Where name = ‘David’ group by Name, Last_name, Salary, position'''

task_3 = '''Select avg(salary) from departments'''

task_4 = '''Select jobs where Средняя ЗП по должности > Больше ли общей средней ЗП group by  job_title'''
