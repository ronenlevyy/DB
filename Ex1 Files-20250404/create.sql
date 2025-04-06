create table Region(
    Region varchar(30) primary key
);

create table IncomeGroup(
    IncomeGroup varchar(30) primary key
);

create table Country(
    CountryName varchar(60) unique,
    CountryCode varchar(3) primary key,
    Region varchar(30),
    IncomeGroup varchar(30),
    foreign key(Region) references Region(Region),
    foreign key(IncomeGroup) references IncomeGroup(IncomeGroup)
);

create table University(
    Specialized boolean not null,
    Divisions integer,
    phd_granging boolean not null,
    Privet01 boolean not null,
    FoudedYear integer check (FoudedYear>0),
    iau_id1 varchar(30) primary key,
    orig_name varchar(180) not null,
    latitude float,
    eng_name varchar(160) not null,
    longtitue float,
    CountryCode varchar(3) not null,
    foreign key(CountryCode) references Country(CountryCode)
);

create table ClosedAt(
    iau_id1 varchar(30),
    Year integer check (Year>0),
    primary key(iau_id1, Year),
    foreign key(iau_id1) references University(iau_id1)
);

create table AcceptanceRate(
    iau_id1 varchar(30),
    Year integer check (Year>0),
    students5_estimated integer,
    primary key(iau_id1, Year),
    foreign key(iau_id1) references University(iau_id1)
);



