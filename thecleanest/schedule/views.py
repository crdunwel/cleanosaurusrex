
from datetime import datetime, date
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.core.serializers import serialize, deserialize
from schedule.models import Assignment, Debit, Credit

def current_schedule(request):
    """JSON representation of the current schedule."""
    # Get current and future assignments
    assignments = Assignment.objects.filter(date__gte=date.today())
    # Remove deferred assignments
    assignments = [a for a in assignments
                   if a.skipped_by is None]
    assign_json = serialize('json', assignments)
    return HttpResponse(assign_json, mimetype='application/json')

def assignments(request):
    assignments = Assignment.objects.all()
    assign_json = serialize('json', assignments)
    return HttpResponse(assign_json, mimetype='application/json')

def debits(request):
    debits = Debit.objects.all()
    debit_json = serialize('json', debits)
    return HttpResponse(debit_json, mimetype='application/json')

def credits(request):
    credits = Credit.objects.all()
    credit_json = serialize('json', credits)
    return HttpResponse(credit_json, mimetype='application/json')
