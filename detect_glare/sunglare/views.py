from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
import datetime

from pysolar.solar import *


class glareView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        # checking if the input was valid
        if serializer.is_valid():
            serializer.save()

            # grabbing the input data
            lat = serializer.data.get("lat")
            lon = serializer.data.get("lon")
            epoch = serializer.data.get("epoch")
            orientation = serializer.data.get("orientation")

            # changing the Linux epoch time into normal UTC time
            date = datetime.datetime.fromtimestamp(epoch, tz=datetime.timezone.utc)

            # used the get altitude and get azimuth functions provided by the pysolar library
            # if these lines are giving error ensure that the pysolar library is installed
            # the functions used the latitude, longitude and date as input to calculate the angles of the sun
            altitude_deg = get_altitude(lat, lon, date)
            azimuth_deg = get_azimuth(lat, lon, date)

            # checking if the azimuthal difference is less or equal to 30 and if the sun is above the horizon and
            # less than 45 degrees of altitude
            # Assumptions made in this case is that the ground has no elevation
            if abs(orientation - azimuth_deg) <= 30.0 and 45.0 >= altitude_deg >= 0:
                return Response({"glare": "false"})
            else:
                return Response({"glare": "false"})
        return Response(serializer.errors)
