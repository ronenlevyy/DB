create table Country(
    CountryName varchar(30) unique,
    CountryCode varchar(3) primary key,
    Region varchar(30),
    IncomeGroup varchar(30),
);

create table Region(
    Region varchar(30) primary key
);

create table IncomeGroup(
    IncomeGroup varchar(30) primary key
);

create table University(
    Specialized boolean not null,
    Divisions integer,
    phd_granging boolean not null,
    Privet01 boolean not null,
    FoudedYear integer check (FoudedYear>0),
    iau_id1 varchar(30) primary key,
    orig_name varchar(30) not null,
    latitude float,
    eng_name varchar(30) not null,
    longtitue float
);

create table ClosedAt(
    eng_name varchar(30) primary key,
    Year integer check (Year>0),
);

create table AcceptanceRate(
    iau_id1 varchar(30) primary key,
    Year integer check (Year>0) primary key,
    students5_estimated integer
);



