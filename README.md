### Grand-events
Flutterwave's rave implementation using python


Grand-events is a web app based on booking of different varieties of events,you want us to handle through our website whereby you are to make payment where necessary

Rave's API are HTTP based RESTful APIs. API request and response format are in JSON.Rave lets you receive payments locally and globally with no hassles and zero .....


It supports all kinds of payment transactions:

    ..Account charge (NG Banks)

   .. Account charge (International for US and ZAR).

    ..Card Charge (Bake in support for 3DSecure/PIN).

    ..Encryption

    ..Transaction status check (Normal requery flow and xrequery).

    ..Retry transaction status check flow.

    ..Preauth -> Capture -> Refund/void.

    ..Support for USSD and Mcash (Alternative payment methods).

    ..List of banks for NG Account charge. (Get banks list).

    ..Get fees endpoint.



INSTALLATION

##pip install virtualenv and activate it

##pip install flutterwave which installs some other additional features with it such as the pycypto

from pyrave import Payment
   
rave_payment = Payment()

data = {...}


TRANSACTIONS
 
 ##Getting encryption key
 """this is the getKey function that generates an encryption Key for you by passing your Secret Key as a parameter.""" which
 return a tuple of data.
 
 
 def getKey(seckey):
    hashedseckey = hashlib.md5(seckey.encode("utf-8")).hexdigest()
    hashedseckeylast12 = hashedseckey[-12:]
    seckeyadjusted = seckey.replace('FLWSECK-', '')
    seckeyadjustedfirst12 = seckeyadjusted[:12]
    return seckeyadjustedfirst12 + hashedseckeylast1


##Getting encrypted data
To get the encrypted data,  """This is the encryption function that encrypts your payload by passing the text and your 
encryption Key."""

PAYMENT WITH CARD

key = getKey(SECRET_KEY)
encrypted_data = encryptData(key, json.dumps(data))


We have our data which include
    
    
    
    
    
    data = {
        "PBFPubKey": "enter your secret key",
        "cardno": "5438898014560229",
        "cvv": "890",
        "expirymonth": "09",
        "expiryyear": "19",
        .
        .
        .
        
##We validates our payment by using an otp


def validate_payment(transaction_reference, otp=None, ):
    if not otp:
        otp = 'number'
        post_data = {
        "PBFPubKey": PUBLIC_KEY,
        "transaction_reference": transaction_reference, 
        "otp": otp
    }
    
    r = requests.post(SANDBOX_VALIDATE_URL, data=post_data)
    print(r.text)

