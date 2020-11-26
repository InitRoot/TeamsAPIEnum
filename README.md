# TeamsAPIEnum
![Follow on Twitter](https://img.shields.io/twitter/follow/initroott?label=Follow%20&style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/initroot/TeamsAPIEnum)
![GitHub stars](https://img.shields.io/github/stars/initroot/TeamsAPIEnum)

User enumeration of MS users using Teams API. The python script simply performs a GET request to:

	GET https://teams.microsoft.com/api/mt/emea/beta/users/ADDRESS/externalsearchv3

The request requires authentication so a MS Bearer token needs to be provided.
	
## Full Request 
The below is the full request sent and can be used to enumerate users.
	
	GET /api/mt/emea/beta/users/§admin2@microsoft.com§/externalsearchv3 HTTP/1.1	
	Host: teams.microsoft.com	
	User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36	
	Accept-Encoding: gzip, deflate	
	Accept: application/json	
	Connection: close	
	Authorization: XXXXXXXXXXXXXXXXXXXX
	x-ms-client-version: 27/1.0.0.2020111144
	Content-type: application/json; charset=UTF-8




	
	
