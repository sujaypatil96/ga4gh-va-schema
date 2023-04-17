

CREATE TABLE "Activity" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	subtype TEXT, 
	date TEXT, 
	"performedBy" TEXT, 
	input TEXT, 
	output TEXT, 
	"specifiedBy" TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", subtype, date, "performedBy", input, output, "specifiedBy")
);

CREATE TABLE "Agent" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	subtype TEXT, 
	name TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", subtype, name)
);

CREATE TABLE "Coding" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	code TEXT, 
	label TEXT, 
	system TEXT, 
	"systemURL" TEXT, 
	"systemVersion" TEXT, 
	PRIMARY KEY (type, description, extensions, code, label, system, "systemURL", "systemVersion")
);

CREATE TABLE "Contribution" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	subtype TEXT, 
	date TEXT, 
	"performedBy" TEXT, 
	input TEXT, 
	output TEXT, 
	"specifiedBy" TEXT, 
	"contributionMadeTo" TEXT, 
	activity TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", subtype, date, "performedBy", input, output, "specifiedBy", "contributionMadeTo", activity)
);

CREATE TABLE "DataItem" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	contributions TEXT, 
	"dateAuthored" TEXT, 
	"specifiedBy" TEXT, 
	"derivedFrom" TEXT, 
	"reportedIn" TEXT, 
	subtype TEXT, 
	value TEXT, 
	unit TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", contributions, "dateAuthored", "specifiedBy", "derivedFrom", "reportedIn", subtype, value, unit)
);

CREATE TABLE "DataSet" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	contributions TEXT, 
	"dateAuthored" TEXT, 
	"specifiedBy" TEXT, 
	"derivedFrom" TEXT, 
	"reportedIn" TEXT, 
	subtype TEXT, 
	"releaseDate" TEXT, 
	license TEXT, 
	version TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", contributions, "dateAuthored", "specifiedBy", "derivedFrom", "reportedIn", subtype, "releaseDate", license, version)
);

CREATE TABLE "Document" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	contributions TEXT, 
	"dateAuthored" TEXT, 
	"specifiedBy" TEXT, 
	"derivedFrom" TEXT, 
	"reportedIn" TEXT, 
	subtype TEXT, 
	title TEXT, 
	license TEXT, 
	version TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", contributions, "dateAuthored", "specifiedBy", "derivedFrom", "reportedIn", subtype, title, license, version)
);

CREATE TABLE "Element" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	PRIMARY KEY (type, description, extensions)
);

CREATE TABLE "Entity" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata")
);

CREATE TABLE "EvidenceLine" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	contributions TEXT, 
	"dateAuthored" TEXT, 
	"specifiedBy" TEXT, 
	"derivedFrom" TEXT, 
	"reportedIn" TEXT, 
	subtype TEXT, 
	"targetProposition" TEXT, 
	"evidenceItems" TEXT, 
	"directionOfEvidenceProvided" TEXT, 
	"strengthOfEvidenceProvided" TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", contributions, "dateAuthored", "specifiedBy", "derivedFrom", "reportedIn", subtype, "targetProposition", "evidenceItems", "directionOfEvidenceProvided", "strengthOfEvidenceProvided")
);

CREATE TABLE "Expression" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	value TEXT NOT NULL, 
	system TEXT NOT NULL, 
	"systemURL" TEXT, 
	"systemVersion" TEXT, 
	PRIMARY KEY (type, description, extensions, value, system, "systemURL", "systemVersion")
);

CREATE TABLE "Extension" (
	type TEXT NOT NULL, 
	extensions TEXT, 
	description TEXT, 
	name TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY (type, extensions, description, name, value)
);

CREATE TABLE "InformationEntity" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	contributions TEXT, 
	"dateAuthored" TEXT, 
	"specifiedBy" TEXT, 
	"derivedFrom" TEXT, 
	"reportedIn" TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", contributions, "dateAuthored", "specifiedBy", "derivedFrom", "reportedIn")
);

CREATE TABLE "Method" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	contributions TEXT, 
	"dateAuthored" TEXT, 
	"specifiedBy" TEXT, 
	"derivedFrom" TEXT, 
	"reportedIn" TEXT, 
	subtype TEXT, 
	license TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", contributions, "dateAuthored", "specifiedBy", "derivedFrom", "reportedIn", subtype, license)
);

CREATE TABLE "Proposition" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	subtype TEXT, 
	"propositionText" TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	qualifiers TEXT, 
	negated BOOLEAN, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", subtype, "propositionText", subject, predicate, object, qualifiers, negated)
);

CREATE TABLE "RecordMetadata" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	"recordIdentifier" TEXT, 
	"recordVersion" TEXT, 
	"derivedFrom" TEXT, 
	"dateRecordCreated" TEXT, 
	contributions TEXT, 
	PRIMARY KEY (type, description, extensions, "recordIdentifier", "recordVersion", "derivedFrom", "dateRecordCreated", contributions)
);

CREATE TABLE "Statement" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	contributions TEXT, 
	"dateAuthored" TEXT, 
	"specifiedBy" TEXT, 
	"derivedFrom" TEXT, 
	"reportedIn" TEXT, 
	subtype TEXT, 
	"statementText" TEXT, 
	"confidenceDirection" TEXT, 
	"confidenceLevel" TEXT, 
	"confidenceScore" TEXT, 
	"evidenceDirection" TEXT, 
	"evidenceLevel" TEXT, 
	"evidenceScore" TEXT, 
	conclusion TEXT, 
	"hasEvidence" TEXT, 
	"hasEvidenceLines" TEXT, 
	"hasEvidenceOfTypes" TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", contributions, "dateAuthored", "specifiedBy", "derivedFrom", "reportedIn", subtype, "statementText", "confidenceDirection", "confidenceLevel", "confidenceScore", "evidenceDirection", "evidenceLevel", "evidenceScore", conclusion, "hasEvidence", "hasEvidenceLines", "hasEvidenceOfTypes")
);

CREATE TABLE "StudyResult" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	id TEXT NOT NULL, 
	identifiers TEXT, 
	label TEXT, 
	urls TEXT, 
	xrefs TEXT, 
	"recordMetadata" TEXT, 
	contributions TEXT, 
	"dateAuthored" TEXT, 
	"specifiedBy" TEXT, 
	"reportedIn" TEXT, 
	subtype TEXT, 
	focus TEXT, 
	"dataItems" TEXT, 
	"derivedFrom" TEXT, 
	PRIMARY KEY (type, description, extensions, id, identifiers, label, urls, xrefs, "recordMetadata", contributions, "dateAuthored", "specifiedBy", "reportedIn", subtype, focus, "dataItems", "derivedFrom")
);

CREATE TABLE "Utility" (
	type TEXT NOT NULL, 
	description TEXT, 
	extensions TEXT, 
	PRIMARY KEY (type, description, extensions)
);
