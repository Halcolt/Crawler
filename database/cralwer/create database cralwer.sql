create database crawler
use crawler


create table ProType(
	PType varchar(10),
	ProviderName varchar(255) not null unique,
	constraint PK_providername primary key (ProviderName),
);

create table ProviderDriveOption(
	ProverderOpID int identity(1,1),
	ProviderName varchar(255),
	MaxPeople int,	-- 0 equal to as much as need
	Sduration int,	-- amount of time that the option will not change
	Price float,		-- Price per month
	Capacity int,	-- drive capacity int Gb form
	constraint PK_Op primary key (ProverderOpID),
	constraint FK_Op foreign key (ProviderName) references ProType(ProviderName),
)

create table MoreDriveOption(
	ProverderOpID int,
	MOption varchar(255),
	constraint FK_MoreOpt foreign key (ProverderOpID) references ProviderDriveOption(ProverderOpID)
)

create table ProviderHostOption(
	ProverderOpID int identity(1,1),
	ProviderName varchar(255),
	MaxDomain int,	-- 0 equal to as much as need
	SubDomain int,	-- amount of time that the option will not change
	Price float,	-- Price per month
	Capacity int,	-- drive capacity int Gb form
	constraint PK_Op primary key (ProverderOpID),
	constraint FK_Op foreign key (ProviderName) references ProType(ProviderName),
)

--DROP---------------------------------------
drop table ProviderOption
drop table ProType
drop database crawler
--DROP---------------------------------------