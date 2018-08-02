from django.http import HttpResponse
from django.shortcuts import render
from .models import TransactionModel
import uuid
from .helpers import pay_with_card, validate_payment


def index(request):
    return render(request, 'temp/index.html')

def details_page(request):
    if request.method == "GET":
        return render(request, 'temp/details.html')
    
    # if request.method == "POST":
    #     # print(request.POST)
    #     # ref = uuid.uuid4().hex
    #     # print('ref', ref)
    #     # transaction = TransactionModel(
    #     #     email = request.POST.get('email'),
    #     #     name = request.POST.get('name'),
    #     #     phone_number = request.POST.get('phone_number'),
    #     #     ref = ref
    #     # )
    #     # transaction.save()
    #     return render(request, 'temp/payment.html')

def payment_page(request):
    # if request.method == "GET":
    #     return render(request, 'temp/payment.html')

    if request.method == "POST":
        print(request.POST)
        ref = uuid.uuid4().hex
        print('ref', ref)

        transaction = TransactionModel(
            email = request.POST.get('email'),
            name = request.POST.get('name'),
            phone_number = request.POST.get('phone_number'),
            ref = ref,
            amount = _get_amout(request.POST.get('event_type'))
        )
        transaction.save()
        return render(request, 'temp/payment.html', {'ref': ref})

def token_page(request):
    # if request.method == "GET":
    #     return render(request, 'temp/token.html')
    
    if request.method == "POST":
        
        print(request.POST)
        ref = request.POST.get('ref')
        transaction = TransactionModel.objects.get(ref=ref)
        
        # add details sent from the payment page
        card_number = request.POST.get('card-num-1') + request.POST.get('card-num-2')
        card_number += request.POST.get('card-num-3') + request.POST.get('card-num-4')
        
        transaction.card_number = card_number
        transaction.ccv = request.POST.get('ccv')
        transaction.expiry_month = request.POST.get('exp-month')
        transaction.expiry_year = request.POST.get('exp-year')
        transaction.pin = request.POST.get('pin')
        transaction.save()

        # initiate payment
        flwRef = initiate_payment(transaction)
        print('flwRef after payment init', flwRef)
        return render(request, 'temp/token.html', {'flwRef': flwRef, 'ref': ref})

def transaction_response(request):
    if request.method == "POST":
        # confirm token sent
        ref = request.POST.get('ref')
        flwRef = request.POST.get('flwRef')
        token = request.POST.get('token')
        res = validate_payment(transaction_reference=flwRef, otp=token)
        if res.get('status') == 'success' and res.get("message") == "Charge Complete":
            message = 'Transaction Successful!\
            Your event has been successfully booked, we will get in touch with you shortly!'
            return render(request, 'temp/success.html', {'message': message})
        else:
            message = 'An error occured. {}, please try again!'.format(res.get("message"))
            return render(request, 'temp/token.html', {'flwRef': flwRef, 'ref': ref, 'message': message})


def _get_amout(option):
    if option == 'Wedding Ceremony(Amount=#150,000)':
        return 150,000
    elif option == 'Naming Ceremony(Amount=#80,000)':
        return 80,000
    elif option == 'Birthday Ceremony(Amount=#100,000)':
        return 100,000
    else:
        return 500,000

def initiate_payment(transaction):
    data = {
            "PBFPubKey": "FLWPUBK-4e581ebf8372cd691203b27227e2e3b8-X",
            "cardno": transaction.card_number,
            "cvv": transaction.ccv,
            "expirymonth": transaction.expiry_month,
            "expiryyear": transaction.expiry_year,
            # "currency": "NGN",
            # "country": "NG",
            "amount": transaction.amount,
            "email": transaction.email,
            "phonenumber": transaction.phone_number,
            "IP": "355426087298442",
            "txRef": transaction.ref
        }
    return pay_with_card(data=data)
    