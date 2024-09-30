# Web Application
Demonstration containerized python3 visitor count web application.
App counts every page load, so no session based.


# Build 
Navigate to folder "Level_1_app" and build your app image using `docker build -t visitor-counter-app .`
Image will be built locally.

# Operation
You can run application using `docker run -p 8000:8000 -v /srv/data:/srv/data visitor-counter-app`

Application runs on port "8000". You can expose application on another port e.g. "8080": `docker run -p 8080:8000 -v /srv/data:/srv/data visitor-counter-app`

Your application will be accesible on `http://localhost:8000` or `http://localhost:8080`, depending of your port preference.

Persistence of visitors conut is possible by using data in attached volume `/srv/data/`. When you forget to attach this volume, file "visitCount.txt" with visits data will be created anyway, but inside container and you loose persitence of data when application restarts.
To reset "visitCount.txt" you can simply use: `sudo cp /dev/null /srv/data/visitCount.txt`.

# Requirements
- Physical or Virtual Machine (best with unixlike OS).
- Docker installed

# Known Issues
- not session based - that means every page load is counted.
