bitly API python library
========================

## Installation

    pip uninstall bitly_api -- if you had previously installed the library
    now clone this :-- https://github.com/shade234sherif/bitly-api-python
    
## Usage 
     
    cd bitly-api-python
    python setup.py
    python short.py[url]
    
## Alternative
 
    check here https://github.com/harkerbyte/bitly-free
    

## Run tests

Your username is the lowercase name shown when you login to bitly, your access token can be fetched using the following ( http://dev.bitly.com/authentication.html ):

    curl -u "username:password" -X POST "https://api-ssl.bitly.com/oauth/access_token"

To run the tests either export the environment variable or set it up inline before calling `nosetests`:

    bitly-api-python $ BITLY_ACCESS_TOKEN=<accesstoken> nosetests

## API Documentation

http://dev.bitly.com/

## Socials 

* <a href=https://facebook.com/harkerbyte>Facebook page</a>
* <a href=https://facebook.com/shade234sherif>Main fb acc</a>
