# fetch-rewards-processor

## BUILDING:

1. Start Docker on your local machine
2. Inside of the directory where you'd like this program to live run the following command
```
git clone git@github.com:Jake-Mulhern/fetch-rewards.git
```
3. $ cd fetch-rewards
4. $ touch .env
5. Add the variables from example.env
6. Please get the SECRET_KEY value from someone within the organization
7. $ docker-compose up


TESTING:
1. Send the following in JSON format to the endpoint http://localhost:8000/receipts/process
You can send this to the endpoint in any manner that works for you.  I will give detailed instructions
on testing using curl below
```
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
```


### This can be accomplished with curl

## Testing with curl

### Testing first endpoint
```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "retailer": "M&M Corner Market",
    "purchaseDate": "2022-03-20",
    "purchaseTime": "14:33",
    "items": [
      {
        "shortDescription": "Gatorade",
        "price": "2.25"
      },{
        "shortDescription": "Gatorade",
        "price": "2.25"
      },{
        "shortDescription": "Gatorade",
        "price": "2.25"
      },{
        "shortDescription": "Gatorade",
        "price": "2.25"
      }
    ],
    "total": "9.00"
  }' \
  http://localhost:8000/receipts/process
```

### Testing Second Endpoint
```
curl -X GET http://localhost:8000/receipts/1/points
```