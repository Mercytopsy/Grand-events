import base64
from Crypto.Cipher import DES3
import hashlib

import requests
import json
import datetime



SANDBOX_URL = 'https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/charge'
SANDBOX_VALIDATE_URL = 'https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/validatecharge'
SECRET_KEY = 'FLWSECK-bc98f3248eb35576a8a3be6217d13fab-X'
PUBLIC_KEY = 'FLWPUBK-5737470b7d033f2a26a4ed1cc447c4fb-X'


def getKey(seckey):

    """this is the getKey function that generates an encryption Key for you by passing your Secret Key as a parameter."""
    # seckey = "FLWSECK-6b32914d4d60c10d0ef72bdad734134a-X"
    hashedseckey = hashlib.md5(seckey.encode("utf-8")).hexdigest()
    hashedseckeylast12 = hashedseckey[-12:]
    seckeyadjusted = seckey.replace('FLWSECK-', '')
    seckeyadjustedfirst12 = seckeyadjusted[:12]
    return seckeyadjustedfirst12 + hashedseckeylast12


def encryptData(key, plainText):
    """This is the encryption function that encrypts your payload by passing the text and your encryption Key."""
    blockSize = 8
    padDiff = blockSize - (len(plainText) % blockSize)
    cipher = DES3.new(key, DES3.MODE_ECB)
    plainText = "{}{}".format(plainText, "".join(chr(padDiff) * padDiff))
    encrypted = base64.b64encode(cipher.encrypt(plainText))
    return encrypted


def pay_with_card(data=None):

    if not data:
        data = {
            "PBFPubKey": "FLWPUBK-4e581ebf8372cd691203b27227e2e3b8-X",
            "cardno": "5438898014560229",
            "cvv": "890",
            "expirymonth": "09",
            "expiryyear": "19",
            "currency": "NGN",
            "country": "NG",
            "amount": "10",
            "email": "user@gmail.com",
            "phonenumber": "0902620185",
            "firstname": "temi",
            "lastname": "desola",
            "IP": "355426087298442",
            "txRef": "MC-" + str(datetime.datetime.now()), # your unique merchant reference
            "meta": [{"metaname": "flightID", "metavalue": "123949494DC"}],
            "redirect_url": "https://rave-webhook.herokuapp.com/receivepayment",
            "device_fingerprint": "69e6b7f0b72037aa8428b70fbe03986c"
        }

    key = getKey(SECRET_KEY)
    encrypted_data = encryptData(key, json.dumps(data))

    post_data = {
        'PBFPubKey': PUBLIC_KEY,
        'client': encrypted_data,
        'alg': '3DES-24'
        }
    
    r = requests.post(SANDBOX_URL, data=post_data)
    print(r.text)

    # stage 2
    pin = data.get('pin')
    if not pin:
        data['pin'] = '3310'
    data['suggested_auth'] = "PIN"

    reencrypted_data = encryptData(key, json.dumps(data))

    post_data = {
        'PBFPubKey': PUBLIC_KEY,
        'client': reencrypted_data,
        'alg': '3DES-24'
    }

    r = requests.post(SANDBOX_URL, data=post_data)
    print(r.text)
    transaction_reference = json.loads(r.text).get('data').get('flwRef')
    return transaction_reference
    # validate_payment(transaction_reference)

def validate_payment(transaction_reference, otp=None):
    if not otp:
        otp = '181971713'
    
    post_data = {
        "PBFPubKey": PUBLIC_KEY,
        "transaction_reference": transaction_reference, 
        "otp": otp
    }

    r = requests.post(SANDBOX_VALIDATE_URL, data=post_data)
    print(r.text)
    return r.json()

if __name__ == '__main__':
    pay_with_card()