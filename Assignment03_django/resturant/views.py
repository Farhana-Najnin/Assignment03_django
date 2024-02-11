from django.shortcuts import render

def home(request):
    paragraph = {
        'paragraph' : 'Welcome to Ma Magic, where every dish tells a story. Join us for unforgettable flavors, warm hospitality, and exclusive perks when you share your number for personalized promotions.'    }
    return render(request,'home.html', context = paragraph)