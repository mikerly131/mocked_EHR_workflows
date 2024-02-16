## Plan / Progress / Notes

* Plan on making my own FHIR server as part of this project (not great from what I see on web, but simple enough for me for now)
  - Create two different apps at some point?
    1. A FastAPI client to provide routes / templates for web app mocking EHR workflow, calls FHIR server app
    2. A FHIR server app that interacts with DB, provides data APIs / services for client app
* Creating models for app / DB using ORM (SQLAlchemy), looking into two ways of doing this:
  - Make model classes based on a FHIR spec version:  R4 since it seems most popular in use right now
  - Make model classes that are more generic:  Able to use/store FHIR spec data, but agnostic of version 
* Since doing my own FHIR server, acting like an EHR who provides one like Epic, going to want a DB for data.
  - PostgreSQL can support JSON data types, better for FHIR version agnostic data model
  - SQLlite - easy to use, but probably tighter coupling to FHIR resources for data model


### FHIR Version Specific Model Classes

* Appointment (Resource)
  - has many multi-value elements: ancestor inherited elements, codeableConcepts, references to other resourceTypes
  - can probably not use quite a few optional elements for simplicity to get started.
  - Rule: only proposed or cancelled appointments can be missing start, end elements.
  - Rule: cancellationReason only allowed if appoinment status is cancelled or no-show
  - Rule: Both start and end must be specified or neither.
* AppointmentParticipant (BackboneElement) 
  - required reference for Appointment to be created.
  - Rule: type or actor must be specified
* Patient (Resource)
  - Probably want at least a few instances to schedule appointments for
  - elements tbd
* Provider (Resource)
  - Probably want at least a few instances
  - elements tbd
* Location (Resource)
  - Probably can at least use this actor reference for appointments to have a location where they are scheduled


### FHIR Version Agnostic Model Classes

* Resource
  - Will have a unique id for the resource instance, tracks what is most recent update of resource., created and most recent update dates.
  - Keep track of the FHIR version of the resource instance.
* ResourceVersion
  - Record when version is first created and new one for each update.
