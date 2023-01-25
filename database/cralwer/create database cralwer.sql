create database crawler

create table crawler.ProType(
	PType varchar(10),
	ProviderName varchar(255) not null unique,
	ProviderEXPyear int,
	NumberOfLeakCase int,
	GetAppPoint int,
	constraint PK_providername primary key (ProviderName),
);

create table crawler.ProviderDriveOption(
	ProverderOpID int identity(1,1),
	ProviderName varchar(255),
	MaxPeople int,	-- 0 equal to as much as need
	Sduration int,	-- amount of time that the option will not change
	Price float,		-- Price per month
	Capacity int,	-- drive capacity int Gb form
	constraint PK_Drive_Op primary key (ProverderOpID),
	constraint FK_Drive_Op foreign key (ProviderName) references ProType(ProviderName),
)

create table MoreDriveOption(
	ProverderOpID int,
	MOption varchar(255),
	constraint FK_Drive_MoreOpt foreign key (ProverderOpID) references ProviderDriveOption(ProverderOpID)
)

create table ProviderHostOption(
	ProverderOpID int identity(1,1),
	ProviderName varchar(255),
	MaxDomain int,	-- 0 equal to as much as need
	SubDomain int,	-- amount of time that the option will not change
	Price float,	-- Price per month
	Capacity int,	-- drive capacity int Gb form
	constraint PK_Host_Op primary key (ProverderOpID),
	constraint FK_Host_Op foreign key (ProviderName) references ProType(ProviderName),
)

create table MoreHostOption(
	ProverderOpID int,
	MOption varchar(255),
	constraint FK_Host_MoreOpt foreign key (ProverderOpID) references ProviderHostOption(ProverderOpID)
)

create table ProviderVMOption(
	ProverderOpID int identity(1,1),
	ProviderName varchar(255),
	MaxPeople int,	-- 0 equal to as much as need
	Sduration int,	-- amount of time that the option will not change
	Price float,		-- Price per month
	constraint PK_VM_Op primary key (ProverderOpID),
	constraint FK_VM_Op foreign key (ProviderName) references ProType(ProviderName),
)

create table MoreVMOption(
	ProverderOpID int,
	MOption varchar(255),
	constraint FK_VM_MoreOpt foreign key (ProverderOpID) references ProviderVMOption(ProverderOpID)
)

--DROP---------------------------------------
drop table ProviderDriveOption
drop table ProviderHostOption
drop table MoreDriveOption
drop table MoreHostOption
drop table ProviderDriveOption
drop table ProType
drop database crawler
--DROP---------------------------------------