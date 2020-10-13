from django.shortcuts import render

def lohbs_pick(request):
    return render(request, 'picks/lohbs_pick.html')