from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLShortenForm 
from .models import URL

def home(req):
    if req.method == 'POST':
        url = URLShortenForm(req.POST)
        if url.is_valid():
            id = url.save().id
            return redirect('show', id = id)
    else:
        form = URLShortenForm()
    data = { 'form':form }
    return render(req, 'shortenurls/home.html', data)

def show(req):
    url = get_object_or_404(URL, pk=id)
    data = {
        'url':url
    }
    return render(req, 'shortenurls/show.html', data)

