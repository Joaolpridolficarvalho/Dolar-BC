# Currency-Converter
## 1. Description
This script has as its objective to offer a pack of functions to work with Dollar, so it can be easily imported into your projects.
## 2. Installation
This script is very easy to import, first, is necessary to move it to the directory of your project, after,  you should install all dependencies necessary, for last, is just use the Import statement.
<br> Example:
``` from bs4 import BeautifulSoup
Import re
Import request
Import main
```

## 3. Methods
The script has three methods. Above we will see what are they and their functions.
1.	**Bilder**: This method is responsible for access to the Banco Central page, to fix the form, get the values and process these data. That method receives a date initial and a date final.  Example: ```` d1 = main.Dolar(“13/12/2022”, “14/12/2022”)````
2.	**get_values**: This method returns the Dollar’s prince between the date rage informed. Example: ```` values = d1.get_values() ````
3.	**convert_Reais_in_dollars**: This method receives a value in Reais and returns the values in Dollars. Example: ````conversion = d1. convert_Reais_in_dollars(30.90) ````
## 4. Docker
To use the Docker file of API, you, first, must download the Docker Desktop, after copy the files at branch “Docker” to your computer, then, open a terminal,  and execute the commands below:
````
Docker build -t dollar .
````
Press Enter, then:
````
Docker run -it dollar
````
 **Obs**: The files need to be in the same folder in the folder “app”, which should be created containing the API.
