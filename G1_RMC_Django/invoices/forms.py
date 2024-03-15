from django import forms

class PaymentForm(forms.Form):
    payment_amt = forms.IntegerField(label='Payment Amount', min_value=0)
