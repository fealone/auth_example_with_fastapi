CONTAINER_ID=$(docker ps --filter name=authexamplewithfastapi_mysql_1 -q)
TARGET_IP=$(docker inspect ${CONTAINER_ID}  -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}')
mysql -h ${TARGET_IP} -uexample -ppassword example -e'insert into users (email,name,hashed_password) values("example@example.com","example","$2b$12$sUi6SEyXzXH8qR9wXRHjPeahHPPf4It0nrfL/7c2xRcKdwek7OCKq");'
