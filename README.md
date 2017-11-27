# one-liners

## A Flask RESTful API to get random one liners
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/gluten-free.svg)](http://forthebadge.com)

## What is the one-liners-api?
The one-liners RESTful API lets you fetch a random one liner for use in all sorts of applications.

## Why the one-liners-api?
The one-liners api is for any developer needing some random oneliner in their life or application.

## URL
```
GET: https://one-liners.herokuapp.com/api
```

## Usage
Just do a GET request on the API URL.
```
GET: https://one-liners.herokuapp.com/api
```

## Examples

### cURL
```
curl -X GET \
'https://one-liners.herokuapp.com/api'
```

### Python
```Python
import requests

requests.get('https://one-liners.herokuapp.com/api')
```

### Node.js (es6)
```Javascript
var request = require('request');

let options = {
    url: 'https://one-liners.herokuapp.com/api',
    method: 'GET'
}

request(options, (err, response, body) => {
    if(!err && response.statusCode == 200)
        console.log(body)
});
```
 ### Any browser
 visit the url: https://one-liners.herokuapp.com/api to get a joke. Press refresh button for more jokes.

## License
MIT

## Contact
Contact me here: [kaushalsharma880@gmail.com](mailto:kaushalsharma880@gmail.com)
