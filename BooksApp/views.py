from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
import requests
from BooksApp.models import Books

# Create your views here.


# Get Books details (Json) and insert into database table
def InsertJsonApiView(request):

    api_url = "https://fakerapi.it/api/v1/books?_quantity=100"

    response = requests.get(api_url)

    for Json_data in response.json()['data']:
        Books(**Json_data).save()  # inserting api json data into databse table

    return JsonResponse({'msg': 'data inserted'})


# Funciton to books title from search bar and match from database table and render the title to template

def GetBooksdetailsView(request):

    Json_data = []
    QuerySet = Books.objects.all()
    for val in QuerySet:
        Json_data.append(val)
    return render(request, 'Search_Page.html', {'search_data': Json_data})

# Funtion to show books details as per title seached from searach bar


def GetTitleProductView(request, pk):

    books_details_list = []
    context = {}
    QuerySet = Books.objects.filter(id=pk).values()
    for records in QuerySet:
        books_details_list.append(records)
    context = {'books_retrieved_data': books_details_list}
    return render(request, 'ShowBooksDetails.html', context)

# Function to Edit Books Details

def GetEditApiView(request, pk):
    create_form_dict = {}
    if request.method == 'POST':

        create_form_dict = dict(request.POST)
        create_form_dict.pop('csrfmiddlewaretoken')
        json_data = {k: create_form_dict[k][0] for k in create_form_dict}
        Books.objects.filter(id=pk).update(**json_data)
        return JsonResponse({'msg': 'data updated sucessfully !!'})
    else:
        create_form_dict = []
        return JsonResponse({'error': 'Something went wrong !!'})
