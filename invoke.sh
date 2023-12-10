# Assuming the city is the first argument when running the script
city=$1

curl -X 'POST' \
  "http://0.0.0.0:8007/locaction?city=$city" \
  -H 'accept: application/json'
