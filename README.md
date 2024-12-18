# pyugt patch offline
Allows you to start Pyugt completely offline to use it with LibreTranslate without asking an external site for localization
### Requirements:
- Python (I used 3.6.8)
- pip install ssl flask
- pyugt ( https://github.com/lrq3000/pyugt/ )
- edit the windows "HOSTS" file and add
  127.0.0.1 geolocation.onetrust.com #[pyugt patch offline]
- edit RUN.bat (change the path to folders based on your installation location)
- put the contents of the “certifi” folder in the pyugt installation folder and overwrite
- ##### LibreTranslate (Argos) [localhost:5000]
[LibreTranslate on Docker](https://hub.docker.com/r/libretranslate/libretranslate)
Or there are other ways:
[LibreTranslate Github](https://github.com/LibreTranslate/LibreTranslate)
### Usage:
start the RUN.bat file you will be prompted to type “China” and then everything will work
