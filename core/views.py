from django.shortcuts import render
import csv, io
from django.contrib import messages
from .models import SuicideStat

def index(request):
    template_name = 'core/index.html'

    context = {

    }
    return render(request, template_name, context)



def basicTable(request):
    template_name = 'core/blank.html'

    prompt = {
		'order': 'Order of the CSV should be respectively'
	}

    if request.method == 'GET':
        return render(request, template_name, prompt)
   
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.info(request, "This is not a csv file.")

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = SuicideStat.objects.update_or_create(
            country=column[0],
            year=column[1],
            sex=column[2],
            age=column[3],
            suicides_no=column[4],
            population=column[5],
        )
    context = {

    }
    return render(request, template_name, context)