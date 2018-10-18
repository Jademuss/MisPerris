from django.shortcuts import render

def post_list(request):
    return render(request, 'Misperris/perris_list.html', {})
