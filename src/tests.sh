echo "Testing sending a transaction"
curl -XPOST -H "Content-type: application/json" -d '{
    "meeting_id": "1234",
    "description" : "Fundamentals of IOTA",
    "user_id" : "555",
    "username" : "Ruben",
    "timestamp" : "07/10/2021 - 11:53:45"
    }' 'http://192.168.0.29:5000/api/v1/send'

echo "Testing querying by meeting ID"
curl -X GET http://192.168.0.29:5000/api/v1/meeting/1

echo "Testing querying by user ID"
curl -X GET http://192.168.0.29:5000/api/v1/user/123