from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data=request.get_json()
    source_currency=data['queryResult']['parameters']['unit-currency']['currency']
    amount=data['queryResult']['parameters']['unit-currency']['amount']
    target_currency=data['queryResult']['parameters']['currency-name']
    print(source_currency)
    print(amount)
    print(target_currency)

    cf = fetch_conversion_factor(source_currency,target_currency)
    final_amount= amount * cf
    final_amount=round(amount,2)
    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
    }
    return jsonify(response)
    print(final_amount)
    return "Hello"
def fetch_conversion_factor(source,target):
    url="https://free.currconv.com/api/v8/convert?q={}_{}&compact=ultra&apiKey=07c3e021777db626dcd3".format(source,target)

    response=requests.get(url)
    response=response.json

    return response['{}_{}'.format(source,target)]

if __name__ == "__main__":
    app.run(debug=True)
