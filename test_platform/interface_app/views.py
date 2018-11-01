from django.shortcuts import render


# Create your views here.
def case_manage(request):
    if request.method == "GET":
        return render(request, "case_manage.html", {
            "type": "list"
        })


def api_debug(request):
    if request.method == "GET":
        return render(request, "api_debug.html", {
            "type": "debug"
        })

