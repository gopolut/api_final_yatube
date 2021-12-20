from rest_framework.pagination import BasePagination, PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from  collections import OrderedDict

class CustomPagination(LimitOffsetPagination):
    limit_query_param = 2
    offset_query_param = 1

    def get_paginated_response(self, data):
            return Response([
                'count', self.count,
                'next', self.get_next_link(),
                'previous', self.get_previous_link(),
                'results', data
            ])