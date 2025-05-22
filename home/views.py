from django.shortcuts import render

# View function to render the index page
def index(request):
    """A view to return the index page"""
    # Render and return the 'home/index.html' template
    return render(request, 'home/index.html')

