#!/usr/bin/bash -eu

DISPLAY_NAME=""
DOMAIN=churadata-isucon.cc
RESULT_FILE=/tmp/result.txt

cd ~/bench

./bench \
  -all-addresses "192.168.0.11,192.168.0.12,192.168.0.13" \
  -target "192.168.0.11:443" \
  -jia-service-url http://bench.${DOMAIN}:8080 \
  -prom-out ${RESULT_FILE} \
  -tls

SCORE=$(cat ${RESULT_FILE} | grep score_total | cut -d' ' -f2)

echo "Score: " ${SCORE}

aws --profile=score-board cloudwatch put-metric-data \
  --namespace ChuraDATA-ISUCON \
  --metric-name score \
  --dimensions Team="${DISPLAY_NAME}" \
  --value ${SCORE}