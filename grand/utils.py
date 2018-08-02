# from pyrave import Payment
# from flutterwave import Flutterwave
   
def test(data=None):
    if not data:
        data = {
            "validateOption": "SMS",          # verification method to use - Voice, SMS
            "authModel": "NOAUTH",               # authentication Model - BVN, PIN, NOAUTH
            "cardno": "4842508225502547", # Card Number
            "cvv": "136",                     # Card CVV
            "expirymonth": "10",              # Card expiry month
            "expiryyear": "18",               # Card expiry year
            "bvn": "12345678901",             # (Optional) User BVN, required only for authModel=BVN
            "country": "NG"                   # Country code (NG)
        }
    rave_payment = Payment()
    # print(data)
    payment_with_card = rave_payment.pay(using="card", **data)
    print(payment_with_card)
    encrypted_data = rave_payment.pay(using="card", return_encrypted=True , **data)
    print(encrypted_data)

# def tokenize_card(data=None):
#     flw = Flutterwave("FLWPUBK-5737470b7d033f2a26a4ed1cc447c4fb-X", "FLWPUBK-5737470b7d033f2a26a4ed1cc447c4fb-X", {"debug": True})

#     if not data:
#         data = {
#             "validateOption": "SMS",          # verification method to use - Voice, SMS
#             "authModel": "NOAUTH",               # authentication Model - BVN, PIN, NOAUTH
#             "cardNumber": "4842508225502547", # Card Number
#             "cvv": "136",                     # Card CVV
#             "expiryMonth": "10",              # Card expiry month
#             "expiryYear": "18",               # Card expiry year
#             "bvn": "12345678901",             # (Optional) User BVN, required only for authModel=BVN
#             "country": "NG"                   # Country code (NG)
#         }

#     r = flw.card.tokenize(data)
#     print("{}".format(r.text))

if __name__ == '__main__':
    test()
    # tokenize_card()