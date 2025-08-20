from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import random

def index(request):
    lucky_number=random.randint(1, 100)
    vegetables=["Tomato 🍅", "Potato 🥔", "Carrot 🥕"]
    for vegetable in vegetables:
        print(vegetable)
    person_age=18
    if person_age<18:
        print("Person is a minor.")
    else:
        print("Person is an adult.")

    cities=[
        {"name": "New York","population":"100,000","country": "USA"},
        {"name": "Tokyo", "population":"14,000,000","country": "Japan"},
        {"name": "London", "population":"9,000,000","country": "UK"}
    ]

    context={'lucky_number': lucky_number,"person_age":person_age, 'vegetables': vegetables, 'cities': cities}
    return render(request, 'index.html', context)
