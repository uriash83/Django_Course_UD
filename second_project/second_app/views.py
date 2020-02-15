from django.shortcuts import render
from .models import Topic,WebPage,AccessRecord

def index (request):
    #webpages_list = AccessRecord.objects.order_by('date')
    webpages_list = AccessRecord.objects.all()
    date_dict = {'access_records': webpages_list}
    print(date_dict)
    my_dict = {'insert_content': "HELLO from app"}
    return render(request,'second_app/index.html',context=date_dict)
