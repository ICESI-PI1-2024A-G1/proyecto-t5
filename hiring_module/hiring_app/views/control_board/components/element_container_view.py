from django.shortcuts import render

# Description: Render a view displaying element container information.
# Input: request, count (int), status (str)
# Output: Rendered template
def element_container_view(request, count, status):
    return render(request, 'control_board.html', {'count': count, 'status': status})
