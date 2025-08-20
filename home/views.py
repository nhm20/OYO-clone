from django.shortcuts import render
import random

def index(request):
    lucky_number = random.randint(1, 100)
    vegetables = ["Tomato 🍅", "Potato 🥔", "Carrot 🥕"]
    person_age = 18

    context = {
        "lucky_number": lucky_number,
        "person_age": person_age,
        "vegetables": vegetables,
    }
    return render(request, "index.html", context)
