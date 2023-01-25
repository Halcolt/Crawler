create database crawler;
use crawler;

create table ProType(
	PType varchar(10),
	ProviderName varchar(255) ,
	ProviderEXPyear int,
	NumberOfLeakCase int,
	GetAppPoint int,
	primary key (ProviderName)
)

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
	constraint PK_Drive_Op primary key (ProverderOpID),
	constraint FK_Drive_Op foreign key (ProviderName) references ProType(ProviderName)
)

create table MoreDriveOption(
	ProverderOpID int,
	MOption varchar(255),
	constraint FK_Drive_MoreOpt foreign key (ProverderOpID) references ProviderDriveOption(ProverderOpID)
)

create table ProviderHostOption(
	ProverderOpID int NOT NULL AUTO_INCREMENT,
	ProviderName varchar(255),
	MaxDomain int,	-- 0 equal to as much as need
	SubDomain int,	-- amount of time that the option will not change
	Price float,	-- Price per month
	Capacity int,	-- drive capacity int Gb form
	constraint PK_Host_Op primary key (ProverderOpID),
	constraint FK_Host_Op foreign key (ProviderName) references ProType(ProviderName)
)


select * from protype
select * from ProviderDriveOption
SELECT * FROM ProviderDriveOption WHERE GbPerPrice = 0.0465

SET SQL_SAFE_UPDATES = 0;
UPDATE ProviderDriveOption SET PricePoint=2 WHERE ROUND(GbPerPrice, 7) = 0.0465;

drop table MoreDriveOption
drop table ProviderDriveOption