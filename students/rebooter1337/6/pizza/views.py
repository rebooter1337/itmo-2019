# -*- coding: utf-8 -*-

import datetime
from django.http import QueryDict
import json
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pizza.models import Ingredient, Order, Pizza
from pizza.serializers import IngredientSerializer, OrderSerializer, PizzaSerializer
from pizza.mailing import send_mail_on_order

from pizza.statistics import (
    overall_statistics,
    pizza_statistics,
    status_statistics,
)



class IngredientViewSet(viewsets.ModelViewSet):
    """Displays all Ingredient instances."""

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    """Displays all Pizza instances."""

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Displays all Order instances."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['POST'])
def post_order(request):
    """Posts Order and sends email to customer."""

    if request.method == 'POST':
        order_data = request.data
        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid():
            serializer.save()
            order = Order.objects.get(pk=serializer.data['id'])
            order.save()
            order.email_sent = True
            order.save()
        if serializer.errors:
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse(serializer.data, status=200)


@api_view(['GET'])
def get_statistics(request):
    """Counts statistics for Order."""

    today = datetime.datetime.today()
    day_ago = today - datetime.timedelta(hours=24)
    orders_today = Order.objects.filter(order_date__gte=day_ago)

    response = {
        'all': overall_statistics(orders_today),
        'pizzas': pizza_statistics(orders_today),
        'statuses': status_statistics(orders_today),
    }
    return Response(response)
