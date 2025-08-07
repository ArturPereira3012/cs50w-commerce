from django import forms
from .models import AuctionListing, Bid, Comment


class ListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']