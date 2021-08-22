from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .util import get_league, get_matches

class LeagueList(APIView):
    def get(self, request, format=None):

        response = get_league('DIAMOND', 'IV', '1')

        return Response(response, status=status.HTTP_200_OK)

class Matches(APIView):
    def get(self, request, format=None):

        league = request.query_params.get('league', None)

        if (league != None):

            response = get_matches(league)

            if 'Error' in response:
                return Response({}, status=status.HTTP_204_NO_CONTENT)

            units = response.get("units")

            return Response(units, status=status.HTTP_200_OK)

        return Response({"Error: No league parameter defined"}, status=status.HTTP_400_BAD_REQUEST)
