# fetch-rewards-processor

BUILDING:

1. Start Docker on your local machine
2. Inside of the directory where you'd like this program to live run the following
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

*This can be accomplished with httpie
Installing and testing with httpie on mac using homebrew
1. $ brew update
2. $ brew install httpie
3. $ echo '{
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
}' | http POST http://localhost:8000/receipts/process
4. This should return {"id": 1}
5. In the browser, visit http://localhost:8000/receipts/1/process
6. This should display {"points":109}

Installing and testing with httpie on windows using Chocolatey
1. Open Command Prompt as Administrator.
2. Install Chocolatey if you haven't done so already. You can do this by running the following command:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

```
3. $ choco install httpie
4. $ echo '{
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
}' | http POST http://localhost:8000/receipts/process
5. This should return {"id": 1}
6. In the browser, visit http://localhost:8000/receipts/1/process
7. This should display {"points":109}