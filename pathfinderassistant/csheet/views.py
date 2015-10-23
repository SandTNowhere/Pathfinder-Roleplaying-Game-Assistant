from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from django.utils import timezone
from .models import Character

def character_list(request):
    characters = Character.objects.order_by('name')
    return render(request, 'csheet/character_list.html', {'characters': characters})

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'csheet/character_detail.html', {'character': character})

def character_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.author = request.user
            character.save()
            return redirect('csheet.views.character_detail', pk=character.pk)
    else:
        form = PostForm()
    return render(request, 'csheet/character_edit.html', {'form': form})

def character_edit(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save(commit=False)
            character.author = request.user
            character.save()
            return redirect('csheet.views.character_detail', pk=character.pk)
    else:
        form = PostForm(instance=character)
    return render(request, 'csheet/character_edit.html', {'form': form})