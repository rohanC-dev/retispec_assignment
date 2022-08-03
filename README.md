The framework I chose to build the APIs is FastAPI, and for the database I chose MySQL.
Both the Acquisitions API, Patiens API, and the database run in their own docker containers.

The way I would deploy this would be to use some cloud provider like AWS, GCP, or Azure to host the different containers, and they would all be able to communicate with REST APIs, and connect to the database. Right now, the way I'm storing the images is just in the acquisitions container itself, and of course this is not the best way to do this as containers are ephemeral. So when I would deploy this, I would change it to store the images using some cloud service (e.g., Storage Bucket) to have some reliability. I would also use a DBaaS for the same reason as before, as well as managing the database may be easier than having it running in a container.

Instructions for running the project:

Prerequisites: You must have docker installed on your machine
<ol>
  <li>Navigate to https://github.com/rohanC-dev/hospital-management-system</li>
  <li>Clone this repository on your local machine with git clone</li>
  <li>**cd** into the repository and run the command  docker-compose up -d --build </li>
  <li>After it's finished building you should be able to access the different APIs:</li>
  <ul>
    <li>Patients API on localhost:8002</li>
    <li>Acquisitions API on localhost:8003</li>
    <li>MySQL Database on localhost:3306</li>
  </ul>
</ol>

To test the endpoints, navigate to /docs for each API, respectively:
<ul>
    <li>So for the Patients API, navigate to localhost:8002/docs</li>
    <li>for the Acquisitions API, navigate to localhost:8003/docs</li>
</ul>



