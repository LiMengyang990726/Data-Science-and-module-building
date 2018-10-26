import requests

url = "https://www.glassdoor.com/Job/json/details.htm"

querystring = {"pos":"101","ao":"301893","s":"58","guid":"000001668b7ef8f99c61b91b53dcbef9","src":"GD_JOB_AD","t":"SR","extid":"1","exst":"O","ist":"L","ast":"OL","vt":"w","slr":"true","rtp":"0","cs":"1_a9181966","cb":"1539938646642","jobListingId":"2993181973","gdToken":"HTvwR1COWM-x0ho1HQlf1Q:9HpsYJGpfPztLTHqBNp3pZmnputxUBS7luOQsyGBTR37Xzg0hhhSo8M21ydUI8cL7Iv3j_PFWGFy4Ck3pMnBnA:-L7xkqnaCwYsj1kKbu7Y2jSzAGNFq53Bj3AZz1CTDvU"}

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "df9cc79f-2b27-4731-9402-b4485f485d06",
    'user-agent': "OPEN SOURCE"
    }


response = requests.get(url, headers=headers, params=querystring)

print(response.text)
