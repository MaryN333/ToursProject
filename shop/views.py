from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Tour, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    searchTerm = request.GET.get('searchTour')
    if searchTerm:
        tours = Tour.objects.filter(title__icontains=searchTerm)
    else:
        tours = Tour.objects.all()
    return render(request=request, template_name='shop/tours.html', context={'searchTerm': searchTerm, 'tours': tours})


# def index(request):
#     tours = Tour.objects.all()
#     return render(request=request, template_name='shop/tours.html', context={'tours': tours})
    # return HttpResponse("Hello")

@login_required  # <- a decorator to make sure that the view is only accessible to the logged in users
def createreview(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'GET':
        return render(request, 'shop/createreview.html', {'form': ReviewForm(), 'tour': tour})
    else:
        try:
            form = ReviewForm(request.POST)
            # We create and save a new review object from the form's values but do not yet put it into the database (commit=False) because we want to specify the user and movie relationships for the review.
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.tour = tour
            newReview.save()
            return redirect('shop:single_tour', newReview.tour.id)
        except ValueError:
            return render(request, 'shop/createreview.html', {'form': ReviewForm(), 'error': 'bad data passed in'})


def single_tour(request, tour_id):
    # Option 1
    # try:
    #     tour = Tour.objects.get(pk=tour_id)
    #     return render(request, 'shop/single_tour.html', {'tour': tour})
    # except Tour.DoesNotExist:
    #     raise Http404()

    # Option 2
    tour = get_object_or_404(Tour, pk=tour_id)
    persons_number = request.GET.get('calculate')
    total_price = 0
    if persons_number is not None:
        total_price = int(persons_number)*tour.price
        # print("Total price, ", total_price)
    reviews = Review.objects.filter(tour=tour)

    return render(request, 'shop/single_tour.html', {'tour': tour, 'total_price': total_price, 'reviews': reviews})


@login_required
def updatereview(request, review_id):
    # supply the logged-in user to ensure that other users can't access the review – for example, if they manually enter the URL path in the browser. Only the user who created this review can update/delete it.
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        # render ReviewForm we used previously in creating a review, but this time, we pass the review object into the form so that the form's fields will be populated with the object's values, ready for the user to edit. Saves us time!
        return render(request, 'shop/updatereview.html', {'review': review, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('shop:single_tour', review.tour.id)
        except ValueError:
            return render(request, 'updatereview.html', {'review': review, 'form': form, 'error': 'Bad data in form'})


@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('shop:single_tour', review.tour.id)
