## MVP - Create a workflow for an employee of a provider to create an appointment for a patient.

FHIR Resource - Collection of information models that define the data elements, constraints and relationships for a healthcare "business object". 

FHIR Resources:
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

All data in FHIR is derived base class Element
FHIR Elements and Data Types:
<table>
<tr><th>Element</th><th>Data Type</th></tr>
<tr>
<td>
<ul>
<li>resourceType</li>
<li>id</li>
<li>text</li>
<li>identifier</li>
<li>status</li>
<li>cancelationReason</li>
<li>serviceCategory</li>
<li>serviceType</li>
<li>specialty</li>
<li>appointmentType</li>
<li>reasonCode</li>
<li>reasonReference</li>
<li>priority</li>
<li>description</li>
<li>start</li>
<li>end</li>
<li>minutesDuration</li>
<li>slot</li>
<li>created</li>
<li>comment</li>
<li>patientInstruction</li>
<li>basedOn</li>
<li>participant</li>
    <ul>
    <li>type</li>
    <li>actor</li>
    <li>required</li>
    <li>status</li>
    <li>period</li>
    </ul>
<li>requestedPeriod</li>
</ul>
</td>
<td>
<ul>
<li>ResourceType (string)</li>
<li>id</li>
<li>Narrative</li>
<li></li>
</ul>
</td>
</table>

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