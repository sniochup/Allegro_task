# Allegro_task
Simple server implemented in Python language which lists the github repositories, their number of stars and sum of stars for the selected username.

## Installation
Firstly, you need to install the libraries if you don't have them on your computer yet.
```
pip install requests
```
Then go to the directory with server.py file. To start the server on the default localhost 9000 port in command line type:
```
python server.py
```
To choose the number of the localhost port type:
```
      python server.py <PORT_NUMBER>
like: python server.py 8080
```
Now your server is working until you will call keyboard interruption pressing `Ctrl+C` combination.

## Usage
Server handle three types of request which returns the data using the HTTP protocol.

#### HEAD
Return only headers with response code **200**.
To send the _HEAD_ request type in command line:
```
       curl -X HEAD -I localhost:<PORT>
like:  curl -X HEAD -I localhost:9000

       curl -X HEAD -I 127.0.0.1:<PORT>
like   curl -X HEAD -I 127.0.0.1:9000
```

#### GET
Return an information as a json file with response code **200**.
The request should be in below format with username in a path.
To send the _GET_ request type in command line:
```
      curl -X GET localhost:9000/<username>
like: curl -X GET localhost:9000/allegro

      curl -X GET 127.0.0.1:9000/<username>
like: curl -X GET 127.0.0.1:9000/allegro
```

#### POST
Return an information as a json file with response code **200**.
The request should be in below format with username in a quotes after `-d` mark.
To send the _POST_ request type in command line:
```
      curl -X POST -d "<username>" localhost:<PORT>
like: curl -X POST -d "allegro" localhost:9000

      curl -X POST -d "<username>" 127.0.0.1:<PORT>
like: curl -X POST -d "allegro" 127.0.0.1:9000
```

## Possible upgrades
- using authentication tokens to increase github api request limit
- getting more information about the repositories, such as last update or language 
      
## License
[MIT](https://choosealicense.com/licenses/mit/)