from django.shortcuts import render
from home.models import Article

# Create your views here. 
def get_home(request):
    object_list = Article.objects.all()
    return render(request,'home.html', {'object_list': object_list})