# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from restpi.models import UserDetails, EmpolyeeDetails
from .serializer import EmpolyeeDetailsSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from datetime import datetime
from .decorator import is_valid_token
from rest_framework.generics import GenericAPIView
from RestAPIs.pagination import CustomPagination
from django.db.models import Q

# Testing API
@csrf_exempt
def index(request):
    return HttpResponse('Hello there..!')


# Registration API
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        try:
            data = {}
            data = json.loads(request.body)
            users = EmpolyeeDetails.objects.create_user(**data)
            token, created = Token.objects.get_or_create(user=users)
            return HttpResponse(token.key)
        except IntegrityError:
            return JsonResponse({'response': 'User Already Exits.', 'code': 200})


# Login User API
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        username = user_data.get('username', None)
        password = user_data.get('password', None)
        user = EmpolyeeDetails.objects.get(email=username, is_active=True)
        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            user.last_login = datetime.now()
            user.save()
            return JsonResponse({
                'message': 'Login Successful',
                'token': token.key
            })
        else:
            return HttpResponse('Wrong Username or Password')


def serializer_data(query_set):
    serializer_query_data = UserSerializer(query_set, many=True)
    return JsonResponse({'user_list': json.loads(json.dumps(serializer_query_data.data))})

# Get List of Data
@csrf_exempt
@is_valid_token()
def get_list(request):
    queryset = User.objects.filter(is_active=1)
    serializer_data_set = serializer_data(queryset)
    return serializer_data_set


def get_query_set_data(data):
    user_id = data.GET.get('id', None)
    user_last_name = data.GET.get('last_name', None)
    user_first_name = data.GET.get('first_name', None)
    query_data = dict(is_active=1)
    if not user_id is None:
        query_data['id'] = user_id
    elif not user_last_name is None:
        query_data['last_name'] = user_last_name
    elif not user_first_name is None:
        query_data['first_name'] = user_first_name

    result_query = User.objects.filter(**query_data)
    return result_query

#search data
@csrf_exempt
@is_valid_token()
def search_data_by_condition(request):
    try:
        get_query_set_result = get_query_set_data(request)
        if get_query_set_result:
            result_set = serializer_data(get_query_set_result)
            return result_set
        else:
            return JsonResponse({'response': 'Ooops No Data Found..!'})
    except:
        return JsonResponse({'code': 502})


@csrf_exempt
@is_valid_token()
def sort_user_deatils(request, name=None, order=None):
    try:
        user_id = request.GET.get('id', None)
        last_name = request.GET.get('last_name', None)
        first_name = request.GET.get('first_name', None)
        if user_id is not None or user_last_name is not None or user_first_name is not None:
            result_query_set = EmpolyeeDetails.objects.filter(Q(id=user_data) | Q(last_name=last_name) | Q(first_name=first_name))
            print(result_query_set)
            if result_query_set:
                result_set = serializer_data(result_query_set)
                return result_set
    except:
        return HttpResponse('Someting went wrong')


class PaginationView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = EmpolyeeDetails.objects.all() #query set data
    pagination_class = CustomPagination
    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '200',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)


# email Validation
def validate_email(email):
    empolyee = None
    try:
        empolyee = EmpolyeeDetails.objects.get(email=email)
    except EmpolyeeDetails.DoesNotExist:
        return None
    if empolyee != None:
        return email

# Logout User
@csrf_exempt
@is_valid_token()
def logout_user(request):
    token_key = request.META.get('HTTP_AUTHORIZATION', None)
    token = token_key.replace('Token ', '')
    Token.objects.get(key=token).delete()
    return JsonResponse({
        'message': 'Logout Successful'
    })

