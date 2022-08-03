The framework I chose to build the APIs is FastAPI, and for the database I chose MySQL.
Both the Acquisitions API, Patiens API, and the database run in their own docker containers.

The way I would deploy this would be to use some cloud provider like AWS, GCP, or Azure, and have 

Instructions for running the project:

Prerequisites: You must have docker installed on your machine
<ol>
  <li>Navigate to https://github.com/rohanC-dev/hospital-management-system</li>
  <li>Clone this repository on your local machine with git clone</li>
  <li>cd into the repository and run the command  docker-compose up -d --build </li>
  <li>After it's finished building you should be able to access the different APIs:</li>
  <ul>
    <li>Patients API on localhost:8002</li>
    <li>Acquisitions API on localhost:8003</li>
    <li>MySQL Database on localhost:3306</li>
  </ul>
</ol>

To test the endpoints, navigate to /docs for each API, spectively.
So for the Patients API, navigate to localhost:8002/docs
   for the Acquisitions API, navigate to localhost:8003/docs



