from django.shortcuts import redirect,render
def search_redirect(request):
    return redirect('/movies/search.html',name='search')
def custom_404(request,e):
    return render('/movies/404.html',name='404')
