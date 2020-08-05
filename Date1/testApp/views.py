from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def datetimeinfo(request):
    date = datetime.datetime.now()
    h = int(date.strftime("%H"))
    msg = '<h1> Hello Guest Very '
    if h < 12:
        msg = msg + 'Good Morning'
    elif h < 16:
        msg = msg + 'Good Afternoon'
    elif h < 20:
        msg = msg + 'Good Evening'
    else:
        msg = msg + 'Good Night'
    msg = msg + '<h1> <hr>'
    msg = msg + '<h1> Now Server Time is:' + str(date) + '</h1>'
    return HttpResponse(msg)

