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
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'music/details.html'
	def get(self,request):
		data=""
		x=(request.query_params)
		song=request.query_params.get("rank",None)
		if song:
			song=int(song)
			data=Music.objects.filter(rank__exact=song).values('rank',"name","artists","danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","duration_ms","time_signature")
		return Response({'songs': data})

class FilterSongs(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'music/index2.html'
	def get(self,request):
		data=Music.objects.all()
		print(request.query_params)
		mode=request.query_params.get("mode",None)
		loudness=request.query_params.get("loudness",None)
		key=request.query_params.get("key",None)
		danceability=request.query_params.get("danceability",None)

		if mode:
			print(mode)
			data &= Music.objects.filter(mode=mode)
		print("mode data count",data.count())

		if loudness:
			print(loudness)
			if loudness=="<-4.5":
				data &= Music.objects.filter(loudness__lte=-4.5)
				print("ss",data.count())
			elif loudness==">-4.5":
				data &= Music.objects.filter(loudness__gte=-4.5)
				print("ssss",data.count())
		print("dddddddd",data.count())

		if key:
			if key=="<5":
				data &= Music.objects.filter(key__lte=5)
			elif key==">5":
				data &= Music.objects.filter(key__gte=5)

		if danceability:
			print("aaaaaaaaa")
			if danceability=="<0.5":
				data &= Music.objects.filter(danceability__lt=0.500)
				print("lll",data.count())
			elif danceability==">0.5":
				data &= Music.objects.filter(danceability__gt=0.500)
				print("aasss",data.count())


		return Response({'songs': data.values()})












