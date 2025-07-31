# from flask import Flask,request

# app = Flask(__name__)



# @app.route('/',methods = ['POST'])
# def index():
#     data = request.get_json()
    
#     amount =  data['queryResult']['parameters']['unit-currency']['amount']
#     source_currency = data['queryResult']['parameters']['unit-currency']['currency']
#     target_currency = data['queryResult']['parameters']['currency-name']
    
#     print(source_currency)
#     print(amount)
#     print(target_currency)
#     return "<h1>hello world</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    
    # Get unit-currency safely
    unit_currency_data = data['queryResult']['parameters'].get('unit-currency', [])

    # If it's a list, take the first element
    if isinstance(unit_currency_data, list) and len(unit_currency_data) > 0:
        unit_currency_data = unit_currency_data[0]

    # Extract values safely
    amount = unit_currency_data.get('amount', 0)  # Default to 0 if missing
    source_currency = unit_currency_data.get('currency', "Unknown")
    target_currency = data['queryResult']['parameters'].get('currency-name', "Unknown")
    
    print(f"Source Currency: {source_currency}")
    print(f"Amount: {amount}")
    print(f"Target Currency: {target_currency}")

    return "<h1>hello world</h1>"

if __name__ == "__main__":
    app.run(debug=True)
