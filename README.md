The framework I chose to build the APIs is FastAPI, and for the database I chose MySQL.
Both the Acquisitions API, Patients API, and the database run in their own docker containers.

The way I would deploy this would be to use some cloud provider like AWS, GCP, or Azure to host the different containers, and they would all be able to communicate with REST APIs, and connect to the database. Right now, the way I'm storing the images is just in the acquisitions container itself, and of course this is not the best way to do this as containers are ephemeral. So when I would deploy this, I would change it to store the images using some cloud storage service (e.g., Storage Bucket) to have some reliability. I would also use a DBaaS for the same reason as before, as well as managing the database may be easier than having it running in a container.

Instructions for running the project:

Prerequisites: You must have docker installed on your machine
<ol>
  <li>Navigate to https://github.com/rohanC-dev/retispec_assignment</li>
  <li>Clone this repository on your local machine with <b>git clone</b></li>
  <li><b>cd</b> into the repository and run the command  <b>docker-compose up -d --build</b> </li>
  <li>After it's finished building you should be able to access the different APIs:</li>
  <ul>
    <li>Patients API on <b>localhost:8002</b></li>
    <li>Acquisitions API on <b>localhost:8003</b></li>
  </ul>
  <li>To test the endpoints, navigate to <b>/docs</b> for each API, respectively:</li>
    <ul>
      <li>So for the Patients API, navigate to <b>localhost:8002/docs</b></li>
      <li>For the Acquisitions API, navigate to <b>localhost:8003/docs</b></li>
      <li>Then you can open the dropdowns, click "Try it out", add the parameters, and then click "Execute" and see the response sent back</li>
    </ul>
</ol>

You could also use some other tool to test the endpoints of course (e.g., Postman).

The database intially has this data when the project is first built, you made need this to test certain endpoints if you will not create any records first:

<img src="https://i.imgur.com/ivLyBPY.pngY"/> <img src="https://i.imgur.com/dxXADyN.png"/>




