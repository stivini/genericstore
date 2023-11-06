from django.shortcuts import render
from .forms import PaymentForm
from .models import PaymentDeets
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0716551972'
    account_reference = 'stephen kiama'
    amount = 1
    transaction_desc = 'daraja 2.0 to the world'
    callback_url = "https://darajambili.herokuapp.com/express-payment"
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
    data = request.body
        
    return HttpResponse("STK Push in Django👋")

# create a new view for clients to input their phone number through forms
def phone_Number_prompt(request):
    info = PaymentDeets.objects.get(name__startswith = 'kiama')
    if request.method=='POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone_no"]

            info.phone_no = phone
            info.amount = amt
            info.save()
            return render(request, 'payment.html',{'phone':phone})
    else:
        form = PaymentForm()
    return render(request, "payment.html", {'form':form})
    