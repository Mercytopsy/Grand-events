from django.conf.urls import url
from . import views

urlpatterns = [
    # /grand/
    url(r'^$', views.index, name="index"),
    url(r'pay', views.payment_page, name="payment_page"),
    url(r'details', views.details_page, name="details_page"),
    url(r'token', views.token_page, name="token_page"),
    url(r'result', views.transaction_response, name="trans_result_page")    
]