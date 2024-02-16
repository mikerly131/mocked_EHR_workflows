## MVP - Create a workflow for an employee of a provider to create an appointment for a patient.

FHIR is a standard for health care data exchange, published by HL7®: https://www.hl7.org/fhir/R4/index.html

FHIR Resource - Collection of information models that define the data elements, constraints and relationships for a healthcare "business object". 

FHIR Resources for MVP:
<table><tr><td>
<ul>
<li>Appointment
<li>AppointmentParticipant (child resource / backbone)
<li>(Conditional) AppointmentResponse
<li>(Conditional) ServiceRequest
<li>(Conditional) Slot
<li>(Conditional) Schedule
<li>(Conditional) Observation
<li>(Conditional) Condition
<li>(Conditional) Procedure
</ul></td>
<td><ul>
<li>(Conditional) ImmunizationRecommendation
<li>(Conditional) Patient
<li>(Conditional) Practitioner
<li>(Conditional) PractitionerRole
<li>(Conditional) RelatedPerson
<li>(Conditional) Device
<li>(Conditional) HealthcareService
<li>(Conditional) Location
</ul></td>
</table>

_not using supportingInformation, for mvp, as any resource can be referenced there._


Should the data model for DB match FHIR specification?
- Maybe, but seems to only be an idea worth considering if using a DB that supports JSON objects
- Ex. PostgreSQL jsonb
- There are performance tradeoffs to consider using Text or JSON data type fields and having to parse or serialize them out of the DB.
- The tradeoffs are with wider relational tables or going nosql like mongo.
- I don't fully understand the performance impacts, don't think I'll know until I try it multiple ways and see for myself.

Assume it doesn't match perfectly, where will data transformation and business logic be implemented?
- Use a Model-View-ViewController Arc?  Do I really know what that means?
-- Views: the routes that serve up the workflow as a web-app, along with templates with html/css/js (or htmx)
-- Model: the classes defined for ORM to interact with DB, going to use SQLAlchemy
-- ViewController:  View models and services to contain transform data for use in/by view, and CRUD on it with DB, any additional business logic.

Will I user a framework for creating web-apps to make this easier?
- Yea, thinking I'm going to use FastAPI - it uses starlette, pydantic, sqlalchemy, jinja or chameleon, etc.

How will authentication / authorization be implemented for the web-app and exposed APIs?
- oAuth2 is the standard for FHIR Servers.  Assuming the back-end is considered a "FHIR Server", then should try for this.
- I thought oAuth2 is more for data APIs exposed over web, and cookies/sessions for users in a web app.  Will need to learn more.