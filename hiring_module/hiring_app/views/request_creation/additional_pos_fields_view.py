from django.http import HttpResponse
from django.template.loader import render_to_string

# Description: Render the additional fields template.
# Input: request (HttpRequest): The HTTP request.
# Output: HttpResponse: Rendered additional fields HTML.
def get_additional_fields(request):
    additional_fields_html = render_to_string('request_creation/partials/course_schedule.html')
    return HttpResponse(additional_fields_html)
