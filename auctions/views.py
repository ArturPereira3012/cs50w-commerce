from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, AuctionListing, Bid, Comment
from .forms import ListingForm, BidForm, CommentForm


def index(request):
    listings = AuctionListing.objects.filter(is_active=True)
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect("index")
    else:
        form = ListingForm()
    return render(request, "auctions/create.html", {
        "form": form
    })


def listing_view(request, listing_id):
    listing = get_object_or_404(AuctionListing, pk=listing_id)
    in_watchlist = request.user.is_authenticated and listing in request.user.watchlist.all()
    is_owner = request.user == listing.owner
    is_winner = (not listing.is_active) and listing.winner() == request.user

    if request.method == "POST":
        if "place_bid" in request.POST:
            bid_form = BidForm(request.POST)
            if bid_form.is_valid():
                bid = bid_form.cleaned_data['amount']
                if bid >= listing.starting_bid and bid > listing.current_price():
                    Bid.objects.create(user=request.user, listing=listing, amount=bid)
                else:
                    return render(request, "auctions/listing.html", {
                        "listing": listing,
                        "bid_form": bid_form,
                        "comment_form": CommentForm(),
                        "message": "Invalid bid.",
                        "in_watchlist": in_watchlist,
                        "is_owner": is_owner,
                        "is_winner": is_winner,
                        "comments": listing.comments.all()
                    })
        elif "add_comment" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                Comment.objects.create(
                    user=request.user,
                    listing=listing,
                    content=comment_form.cleaned_data['content']
                )
        elif "close_auction" in request.POST and is_owner:
            listing.is_active = False
            listing.save()
        elif "watchlist_add" in request.POST:
            request.user.watchlist.add(listing)
        elif "watchlist_remove" in request.POST:
            request.user.watchlist.remove(listing)

        return redirect("listing", listing_id=listing_id)

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bid_form": BidForm(),
        "comment_form": CommentForm(),
        "comments": listing.comments.all(),
        "in_watchlist": in_watchlist,
        "is_owner": is_owner,
        "is_winner": is_winner
    })


@login_required
def watchlist_view(request):
    return render(request, "auctions/watchlist.html", {
        "listings": request.user.watchlist.all()
    })


def categories_view(request):
    categories = AuctionListing.objects.values_list('category', flat=True).distinct().exclude(category__isnull=True)
    return render(request, "auctions/categories.html", {
        "categories": categories
    })


def category_listings(request, category):
    listings = AuctionListing.objects.filter(category=category, is_active=True)
    return render(request, "auctions/category.html", {
        "category": category,
        "listings": listings
    })
