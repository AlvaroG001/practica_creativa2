FROM ruby:2.7.1-slim

WORKDIR /opt/microservices

COPY practica_creativa2/bookinfo/src/details/details.rb /opt/microservices/


EXPOSE 9080

ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

CMD ["ruby", "details.rb", "9080"]