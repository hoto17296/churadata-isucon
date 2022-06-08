#!/usr/bin/bash -eu

DOMAIN=churadata-isucon.cc

cd ~/bench

./bench \
  -all-addresses app-1.${DOMAIN} \
  -target app-1.${DOMAIN}:443 \
  -jia-service-url http://bench.${DOMAIN}:8080 \
  -tls