# url-shortening-app
To run locally clone this repo to your machine and run:
- `$ cd url-shortening-service`
- `$ make build`

After successful launch go to localhost:8000/docs in your browser to browse
the docs and test APIs.

## Available APIs:

| Resource         | Method | Description                                                                                                      |
|------------------|--------|------------------------------------------------------------------------------------------------------------------|
| /{shortened_url} | GET    | Navigate to original url with shortened url                                                                      |
| /shorten_url     | POST   | Shortens given url and returns shortened url. Request body: url: string (required), valid_days: int (optional)   | 

