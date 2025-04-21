from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TestForm
from .models import Test

@login_required
def test_create(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.created_by = request.user
            return redirect('test_list')  
    else:
        form = TestForm()

    return render(request, 'test_create.html', {'form': form})


def index(request):
    return render(request, 'index.html')

# def test_list(request):
#     tests = Test.objects.all()
#     return render(request, 'tests.html', {'tests': tests})

from django.shortcuts import render, get_object_or_404
from .models import Category, Baza, Test

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'quiz/category.html', {'categories': categories})


def baza_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    bazas = Baza.objects.filter(category=category)
    return render(request, 'quiz/baza.html', {
        'category': category,
        'bazas': bazas
    })


def test_list(request, baza_id):
    baza = get_object_or_404(Baza, id=baza_id)

    # View ni oshiramiz
    baza.view += 1
    baza.save()

    tests = Test.objects.filter(baza=baza)
    return render(request, 'quiz/test.html', {'baza': baza, 'tests': tests})
