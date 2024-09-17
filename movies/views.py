from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.decorators import login_required
from .models import Movie,Booking,Wallet
from django.contrib import messages
from .forms import BalanceUpdateForm


def home(request):
    context = {
        'posts': Movie.objects.all()
    }
    return render(request, 'movies/home.html', context)


class PostListView(ListView):
    model = Movie
    template_name = 'movies/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'movies'
    ordering = ['-launch_date']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Movie

def about(request):
    return render(request, 'movies/about.html', {'title': 'About'})


### booking


@login_required
def bookmovie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    wallet = get_object_or_404(Wallet, user=request.user)
    if not Booking.objects.filter(user=request.user, movie=movie).exists():
        Booking.objects.create(user=request.user, movie=movie)
        Wallet.deduct_funds(request.user,movie.price)
        return render(request, 'movies/booking_success.html')
    else:
        return render(request,'movies/already_booked.html')
def booking_success(request):
    return render(request, 'movies/booking_success.html') 
def already_booked(request):
    return render(request, 'movies/already_booked.html') 

def bookinglist(request):
    Bookings = Booking.objects.filter(user=request.user)
    return render(request, 'movies/bookings.html', {'Bookings': Bookings})




@login_required
def updatebalance(request):
    if request.method == 'POST':
        b_form = BalanceUpdateForm(request.POST, instance=request.user)
        if b_form.is_valid():
            b_form.save()
            messages.success(request, f'Your balamce has been updated!')
            return redirect('profile')

    else:
        b_form = BalanceUpdateForm(instance=request.user)

    context = {
        'b_form': b_form
    }

    return render(request, 'movies/balance.html', context)
