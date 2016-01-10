from django.shortcuts import render_to_response, RequestContext


def index(request):
    context = RequestContext(request)
    context_list = {
        'site_title': "Aansi CMS",
        'greeting_title': "Welcome",
        'greeting_description': "Aansi CMS Up and Running"
    }
    return render_to_response("welcome/index.html", context_list, context)


