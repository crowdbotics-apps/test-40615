from rest_framework import authentication
from offer.models import Offer
from .serializers import OfferSerializer
from rest_framework import viewsets

class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Offer.objects.all()