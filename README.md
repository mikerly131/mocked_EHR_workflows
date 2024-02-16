# mocked_EHR_workflows
Rewriting an application to mock EHR workflows with FHIR integrations

## Current Plan / Progress
* Figure out an app architecture to try, because that is how I'm thinking about this project:  Maybe MVC. 
* Pick an MVP workflow to create:  Schedule an appointment for a patient.
* Determine the FHIR resources that will be needed to persist / read /search workflow data on a FHIR Server.
* Which FHIR server / sandbox to use:  Epic? Make my own FHIR server?
* Create a DB for the FHIR Server if using my own, mock up something like an EHR would use. 
  - Data model that is more tightly coupled to specific FHIR Versions or less coupled, version agnostic?
  - Use a DB that supports JSON data types?  If not, serialize / deserialize with service?
* Figure out what fhir-py, smart-on-fhir/client-py, fhirpath-py and FHIRpath in general all do and why.
  - Been reviewing docs and examples and it is not much clearer yet what benefits these provide me.
  - In general, I'm too novice at app dev and FHIR to understand these well.
    - Beda's fhir-py seems like app or package that can be used to create pythonic data from FHIR resources to be easier to work with
    - Client-py seems to be a data translation? transformation? package like fhir-py but with explicit models by FHIR version.
    - fhirpath-py isn't making sense to me, doesn't fhir-py already provide data in pythonic way that can be traversed?
* Start with figuring out Resources, their elements and data types that are used for scheduling an appointment.
  - If making up own server, probably use ORM (SQLAlchemy) and create some model classes / tables for MVP
* Use a web app framework to make things simpler for myself:  FastAPI most likely
  - Models: Appointment and other resources for scheduling appointment, elements, typing 
  - Services:  Serialize/Deserialize data, CRUD functions, business logic?
  - View Models:  Think this would be for creating objects and transforming data for presentation in workflow / templates.
  - Views:  Routes & functions that will provide the functionality for the workflows / templates.