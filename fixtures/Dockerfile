FROM mongo
WORKDIR /test
ADD test /test
CMD mongorestore --host mongodb --db test /test
