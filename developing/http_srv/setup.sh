docker run -d --name weather -p 5555:5432 -e POSTGRES_DBNAME=test \
    -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test postgres

psql -h 127.0.0.1 -p 5555 -U test test
