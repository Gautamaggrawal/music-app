from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import generics
from .serializers import SongsSerializer
from django.db.models import Q
class SearchSong(APIView):
	# renderer_classes = [TemplateHTMLRenderer]
	# template_name = 'profile_list.html'
	def get(self,request):
		queryset='Not Found'
		search=request.query_params.get("q",None)	
		if search:
			queryset=Music.objects.filter(Q(name__icontains=search) |Q(artists__icontains=search) ).values("name")
		return Response({"musicsearches":queryset})

class DisplayTopView(generics.ListAPIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'music/index.html'
	def get(self,request):
		queryset=Music.objects.all().order_by("rank")
		serializer_class = SongsSerializer
		return Response({'songs': queryset})


class SongsDetails(APIView):
	def get(self,request):
		data=""
		song=request.query_params.get("song",None)
		if song:
			data=Music.objects.filter(name__exact=song).values('rank',"name","artists","danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","duration_ms","time_signature")
		return Response({'songs': data})













