from django.shortcuts import render_to_response

# Create your views here.


def main(request):
    return render_to_response('main/base1.html')