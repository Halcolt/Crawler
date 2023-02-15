drop database crawler
create database crawler
use crawler

create table ProType(
	PType varchar(10),
	ProviderName varchar(255) ,
    NumberOfOption int,
	GetAppPoint float,
	primary key (ProviderName)
);

create table ProviderDriveOption(
	ProverderOpID int NOT NULL AUTO_INCREMENT,
	ProviderName varchar(255),
	MaxPeople int,	-- 0 equal to as much as need
	Sduration int,	-- amount of time that the option will not change
	Price float,	-- Price per month
	Capacity int,	-- drive capacity int Gb form
	GbPerPrice float,
    PricePoint int,
    PeoplePoint int,
    AveragePoint float,
	constraint PK_Drive_Op primary key (ProverderOpID),
	constraint FK_Drive_Op foreign key (ProviderName) references ProType(ProviderName)
);


create table MoreDriveOption(
	MoreOptID int PRIMARY KEY AUTO_INCREMENT,
	ProverderOpID int,
	MOption varchar(255),
	constraint FK_Drive_MoreOpt foreign key (ProverderOpID) references ProviderDriveOption(ProverderOpID)
);

create table ProviderHostOption(
	ProverderOpID int NOT NULL AUTO_INCREMENT,
	ProviderName varchar(255),
    Sduration int,	-- amount of time that the option will not change
	-- MaxDomain int,	-- 0 equal to as much as need
	-- SubDomain int,	-- amount of time that the option will not change
	Price float,	-- Price per month
    Core int,
    Ram int,
	Capacity int,	-- drive capacity int Gb form
	Bandwidth int,
    PricePoint float,
    CPUPoint int,
    RamPoint int,
	Bandpoint int,
    AveragePoint float,
	constraint PK_Host_Op primary key (ProverderOpID),
	constraint FK_Host_Op foreign key (ProviderName) references ProType(ProviderName)
);

CREATE TABLE MoreHostOption(
  MoreOptID int PRIMARY KEY AUTO_INCREMENT,
  ProverderOpID int,
  MOption varchar(255),
  CONSTRAINT FK_Host_MoreOpt FOREIGN KEY (ProverderOpID) REFERENCES ProviderHostOption(ProverderOpID)
);

select * from protype;
select * from ProviderDriveOption
select * from ProviderHostOption
select * from MoreHostOption
select * from MoreDriveOption

UPDATE ProviderHostOption SET AveragePoint = (PricePoint + CPUPoint + RamPoint + BandPoint)/4
-- SELECT * FROM ProviderDriveOption WHERE GbPerPrice = 0.0465

SET SQL_SAFE_UPDATES = 0;
UPDATE ProviderDriveOption SET GbPerPrice = Price / Capacity;


drop table MoreDriveOption
drop table MoreHostOption
drop table ProviderDriveOption
drop table ProviderHostOption
drop table Protype