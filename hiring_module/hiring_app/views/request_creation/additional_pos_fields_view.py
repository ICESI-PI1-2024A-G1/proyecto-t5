from django.http import HttpResponse
from django.template.loader import render_to_string

def get_additional_fields(request):
    # Render the additional fields template
    additional_fields_html = render_to_string('request_creation/partials/course_schedule.html')
    return HttpResponse(additional_fields_html)
