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
    edit_json_dict = {}
    if request.method == 'POST':
        if request.user.is_superuser: # checking if the user is admin 

            edit_json_dict = dict(request.POST)
            edit_json_dict.pop('csrfmiddlewaretoken')
            json_data = {k: edit_json_dict[k][0] for k in edit_json_dict}
            Books.objects.filter(id=pk).update(**json_data)
            return JsonResponse({'msg': 'data updated sucessfully !!'})
        else:

            return JsonResponse({'error': 'You cannnot access the Api'})
    else:
        edit_json_dict = []
        return JsonResponse({'error': 'Something went wrong !!'})
