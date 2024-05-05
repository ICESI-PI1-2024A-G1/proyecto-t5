from django.shortcuts import render

def element_container_view(request, count, status):
    return render(request, 'control_board.html', {'count': count, 'status': status})
