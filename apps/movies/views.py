from django.shortcuts import render
from django.shortcuts import render, redirect
from apps.movies.models import Category, Movie, Series
from apps.users.models import  Comments, Likes, DisLikes, Reviews
from apps.settings.models import Settings
from django.db.models import Sum, Count
from django.db.models import Q
# Create your views here.
def movie_detail(request, id):
    setting=Settings.objects.latest('id')
    categories = Category.objects.all()
    movie=Movie.objects.get(id=id)
    recomandations = Movie.objects.all().order_by('?')
    if request.method == 'POST':
        movie=Movie.objects.get(id=id)
        if 'comment' in request.POST:
            text = request.POST.get('text')
            parent=request.POST.get('parent')
            user=request.user
            if parent:
                comment=Comments.objects.create(user=request.user, text=text, movie=movie, parent_id=parent)
                comment.save()
                return redirect('movie_detail', movie.id)
            else:
                comment=Comments.objects.create(user=request.user, text=text, movie=movie)
                comment.save()
                return redirect('movie_detail', movie.id)
        if 'comment_likes' in request.POST or 'son_like' in request.POST :
            movie=Movie.objects.get(id=id)
            comment_id=request.POST.get('comment_id')
            try:
                like=DisLikes.objects.get(user=request.user, comment_id=comment_id)
                like.delete()
                try:    
                    like=Likes.objects.get(user=request.user, comment_id=comment_id)
                    like.delete()
                except:
                    Likes.objects.create(user=request.user, comment_id=comment_id)
            except:
                try:    
                    like=Likes.objects.get(user=request.user, comment_id=comment_id)
                    like.delete()
                except:
                    Likes.objects.create(user=request.user, comment_id=comment_id)
            return redirect('movie_detail', movie.id)
        if 'comment_dislikes' in request.POST or 'son_dislike' in request. POST :
            movie=Movie.objects.get(id=id)
            comment_id=request.POST.get('comment_id')
            try:
                like=Likes.objects.get(user=request.user, comment_id=comment_id)
                like.delete()
                try:    
                    like=DisLikes.objects.get(user=request.user, comment_id=comment_id)
                    like.delete()
                except:
                    DisLikes.objects.create(user=request.user, comment_id=comment_id)
            except:
                try:    
                    like=DisLikes.objects.get(user=request.user, comment_id=comment_id)
                    like.delete()
                except:
                    DisLikes.objects.create(user=request.user, comment_id=comment_id)
            return redirect('movie_detail', movie.id)
        if 'review' in request.POST:
            title=request.POST.get('title')
            text=request.POST.get('text')
            rating=request.POST.get('rating')
            review=Reviews.objects.create(user=request.user, movie=movie, title=title, text=text, number=rating)
            mid_rate = movie.review_movie.aggregate(
                numbers = Sum('number'),
                len = Count('id')
            )
            movie.rating = float(str(mid_rate['numbers'] / mid_rate['len'])[:4])
            movie.save()
            review.save()
            return redirect('movie_detail', movie.id)
        if 'delete' in request.POST:
            try:
                comment_id = request.POST.get('id')
                comment = Comments.objects.get(id = comment_id) 
                comment.delete()
            except:
                review_id = request.POST.get('id')
                review = Reviews.objects.get(id = review_id)
                review.delete() 
            return redirect('movie_detail', movie.id)
    context = {
        'setting' : setting,
        'movie' : movie,
        'recomandations' : recomandations,
        'categories' : categories,
    }
    return render (request, 'movies/details.html', context)

def movie_catalog(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug = slug)
    movies = Movie.objects.filter(category=category)
    setting=Settings.objects.latest('id')
    context = {
        'setting' :  setting,
        'movies' :  movies,
        'category' : category,
        'categories' : categories,
    }
    return render(request, 'movies/catalog.html', context)

def series(request, id):
    recomandations = Movie.objects.all().order_by('?')
    setting = Settings.objects.latest('id')
    series = Series.objects.get(id=id)
    tv_series = Series.objects.filter(series=series.series)
    categories = Category.objects.all()
    context = {
        'setting': setting,
        'series': series,
        'categories':categories,
        'recomandations':recomandations,
        'tv_series':tv_series,
    }
    return render(request, 'movies/series.html', context)

def search(request):
    search_key = request.GET.get('key')
    setting = Settings.objects.latest('id')
    categories = Category.objects.all()
    movie=Movie.objects.all()
    if search_key:
        movie = Movie.objects.filter(Q(title__icontains = search_key[0].title()+ search_key[1::]))
    context = {
        'setting':setting,
        'movie':movie, 
        'categories':categories,
    }
    return render(request, 'movies/search.html', context)
   
    
    