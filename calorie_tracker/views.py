from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import FoodItem
from .forms import FoodItemForm

def index(request):
    items = FoodItem.objects.all()
    total_calories = sum(i.calories for i in items)
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('calorie_tracker:index'))
    else:
        form = FoodItemForm()
    return render(request, 'calorie_tracker/index.html', {
        'items': items,
        'total_calories': total_calories,
        'form': form,
    })

def delete_item(request, pk):
    item = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        item.delete()
    return redirect('calorie_tracker:index')

def reset_items(request):
    if request.method == 'POST':
        FoodItem.objects.all().delete()
    return redirect('calorie_tracker:index')
