import os
import sys

base_path = os.path.dirname(os.path.dirname(os.path.join('..', os.path.realpath(__file__))))
sys.path.append(base_path)

from grand.helpers import pay_with_card, validate_payment

import unittest



MOCK_DATA = {
        "PBFPubKey": "FLWPUBK-4e581ebf8372cd691203b27227e2e3b8-X",
        "cardno": "5438898014560229",
        "cvv": "890",
        "expirymonth": "09",
        "expiryyear": "19",
        "currency": "NGN",
        "country": "NG",
        "amount": "10",
        "pin": "3310",
        "email": "user@gmail.com",
        "phonenumber": "0902620185",
        "firstname": "temi",
        "lastname": "desola",
        "IP": "355426087298442",
        "txRef": "MC-" + '2018-08-02 14:52:29.3744', # your unique merchant reference
        "meta": [{"metaname": "flightID", "metavalue": "123949494DC"}],
        "redirect_url": "https://rave-webhook.herokuapp.com/receivepayment",
        "device_fingerprint": "69e6b7f0b72037aa8428b70fbe03986c"
    }

MOCK_SUCCESS_RESPONSE = {'status': 'success', 'message': 'Charge Complete', 'data': {'data': {'responsecode': '00', 'responsemessage': 'successful'}, 'tx': {'id': 208870, 'txRef': 'MC-2018-08-02 14:52:29.374475', 'orderRef': 'URF_1533217979797_6288335', 'flwRef': 'FLW-MOCK-3a7f355c97f1f82c81ab1dc9a8fbc1da', 'redirectUrl': 'https://rave-webhook.herokuapp.com/receivepayment', 'device_fingerprint': '69e6b7f0b72037aa8428b70fbe03986c', 'settlement_token': None, 'cycle': 'one-time', 'amount': 10, 'charged_amount': 10, 'appfee': 0.14, 'merchantfee': 0, 'merchantbearsfee': 1, 'chargeResponseCode': '00', 'raveRef': 'RV31533217978808D494FFE12C', 'chargeResponseMessage': 'Please enter the OTP sent to your mobile number 080****** and email te**@rave**.com','authModelUsed': 'PIN', 'currency': 'NGN', 'IP': '::ffff:10.136.66.169', 'narration': 'CARD Transaction ', 'status': 'successful', 'modalauditid': 'ca07961a6f8bd4b2676089fba6112653', 'vbvrespmessage': 'successful', 'authurl': 'N/A', 'vbvrespcode': '00', 'acctvalrespmsg': None, 'acctvalrespcode': None, 'paymentType': 'card', 'paymentPlan': None, 'paymentPage': None, 'paymentId': '861', 'fraud_status': 'ok', 'charge_type': 'normal', 'is_live': 0, 'createdAt': '2018-08-02T13:52:59.000Z', 'updatedAt': '2018-08-02T13:53:08.000Z', 'deletedAt': None, 'customerId': 40183, 'AccountId': 6031, 'customer': {'id': 40183, 'phone': '0902620185', 'fullName': 'temi desola', 'customertoken': None, 'email': 'user@gmail.com', 'createdAt': '2018-07-31T21:21:28.000Z', 'updatedAt': '2018-07-31T21:21:28.000Z', 'deletedAt': None, 'AccountId': 6031}, 'chargeToken': {'user_token': '3a310', 'embed_token': 'flw-t0-2c399cc1a5a2ae2581e41f5de596d131-m03k'}}, 'airtime_flag': None}}


class TestQueryAggregator(unittest.TestCase):

    def test_charge_card_endpoint(self):
        transRef = pay_with_card(MOCK_DATA)
        expected_result = {"status":"success","message":"AUTH_SUGGESTION","data":{"suggested_auth":"PIN"}}
        # self.assertEqual(transRef, expected_result)
        self.assertEqual(MOCK_SUCCESS_RESPONSE, validate_payment(transRef))

if __name__ == "__main__":
    unittest.main()