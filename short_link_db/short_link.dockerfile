FROM postgres
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD temp
ENV POSTGRES_DB short_link
ADD create_short_link.sql /docker-entrypoint-initdb.d/