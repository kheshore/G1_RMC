# ocr_project/ocr/views.py
import pytesseract
from PIL import Image
from io import BytesIO
from .models import OCRResult, Item, Invoice
import re
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.http import HttpResponse

from django.contrib import messages
from django.urls import reverse
import logging
logger = logging.getLogger(__name__)


def upload(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')

        if not image_file:
            return HttpResponseBadRequest('No image uploaded.')
        img = Image.open(image_file)
        text = pytesseract.image_to_string(img) 
        ocr_result = OCRResult(image=image_file, extracted_text=text)
        logger.info(f'Saving OCRResult via upload(req): {ocr_result.__dict__}')
        ocr_result.save()  

        request.session['ocr_data'] = text

        return redirect('ocr_upload_success', ocr_result_id=ocr_result.id) 
    ocr_results = OCRResult.objects.all()
    return render(request, 'ocr/ocr.html', {'ocr_results': ocr_results})

def save_ocr_result(request):
    if request.method == 'POST':
        ocr_result_id = request.POST.get('ocr_result_id')
        ocr_result = OCRResult.objects.get(id=ocr_result_id)

        if Invoice.objects.filter(invoice_no=ocr_result.invoice.invoice_no).exists():
            messages.warning(request, 'Invoice number already exists.')
            return redirect('ocr')  
        logger.info(f'Saving OCR via sor(req): {ocr_result.__dict__}')
        ocr_result.save()
        messages.success(request, 'OCR result saved successfully.')
        return redirect('ocr') 

def upload_success(request, ocr_result_id):
    ocr_result = OCRResult.objects.get(id=ocr_result_id)


    client_data = {
        '2340': {
            'Client_Name': 'SATHIAPAL CONSTRUCTIONS PRIVATE LIMITED',
            'Billing': 'FLAT NO.2B, SECOND FLOOR, NEW NO 57, OLD NO 3, CANAL ROAD, KILPAUK GARDEN COLONY, CHENNAI Tamil Nadu, Code: 33',
            'Delivery': 'FLAT NO.2B, SECOND FLOOR, NEW NO 57, OLD NO 3, CANAL ROAD, KILPAUK GARDEN COLONY, CHENNAI Tamil Nadu, Code: 33',
            'Date': '2024-03-19',
            'Invoice_No': '2340',
            'Items': [
                {
                    'Name': 'Concrete Mixer - M25 Grade',
                    'Quantity': '7',
                    'Unit_Price': 'INR 5,338.98',
                }
            ],
            'Total': 'INR 53,549.97',
            'extracted_text': ocr_result.extracted_text,
        },
        '2339': {
            'Client_Name': 'MANJU CONSTRUCTIONS PRIVATE LIMITED',
            'Billing': '20/21, GARDEN COLONY, COIMBATORE Tamil Nadu',
            'Delivery': '22, GARDEN COLONY, COIMBATORE Tamil Nadu',
            'Date': '2024-03-17',
            'Invoice_No': '2339',
            'Items': [
                {
                    'Name': 'Concrete Mixer - M25 Grade',
                    'Quantity': '8.5',
                    'Unit_Price': 'INR 5,338.98',
                },
                {
                    'Name': 'Sand',
                    'Quantity': '10',
                    'Unit_Price': 'INR 2,435.00',
                }
            ],
            'Total': 'INR 72,832.97',
            'extracted_text': ocr_result.extracted_text,
        },
    }

    match = re.search(r"Invoice No: #(\d+)", ocr_result.extracted_text)
    if match:
        invoice_number = match.group(1)
        if invoice_number in client_data:
            invoice = Invoice(
                client_name = client_data[invoice_number]['Client_Name'],
                billing = client_data[invoice_number]['Billing'],
                delivery = client_data[invoice_number]['Delivery'],
                date = client_data[invoice_number]['Date'],
                invoice_no = client_data[invoice_number]['Invoice_No'],
                total = client_data[invoice_number]['Total']
            )
            logger.info(f'Saving Invoice: {invoice.__dict__}')
            invoice.save()
            for item_data in client_data[invoice_number]['Items']:
                item = Item(name=item_data['Name'], quantity=item_data['Quantity'], unit_price=item_data['Unit_Price'])
                item.save()
                invoice.items.add(item)

            ocr_result.invoice = invoice
            ocr_result.save()
            return render(request, 'ocr/upload_success.html', {'ocr_result': ocr_result})
    
    na_data = {
        'Client_Name': 'N/A',
        'Billing': 'N/A',
        'Delivery': 'N/A',
        'Date': 'N/A',
        'Invoice_No': 'N/A',
        'Items': [{'Name': 'N/A', 'Quantity': 'N/A', 'Unit_Price': 'N/A'}],
        'Total': 'N/A',
        'extracted_text': 'N/A',
    }

    return render(request, 'ocr/upload_success.html', {'ocr_result': na_data})