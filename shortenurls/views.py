from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import URLShortenForm 

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

