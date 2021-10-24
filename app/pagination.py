from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from . utils import *
import json

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        # data = json.dumps(data)
        # print('data', data)
        data1 = {'data':{ 
                        'next': self.get_next_link(),
                        'previous': self.get_previous_link(),
                        'count': self.page.paginator.count,
                        'results': data }
                        }
        data1 = json.dumps(data1)
        print('data1', data1)
        data1 = data_encryptor(str(data1))
        return Response({
            "status": 200,
            "message": "Your list",
            'results': data1 }
            )






# DEFAULT_PAGE = 1
# DEFAULT_PAGE_SIZE = 2
#
#
#
# class CustomPagination(PageNumberPagination):
#     page = DEFAULT_PAGE
#     page_size = DEFAULT_PAGE_SIZE
#     page_size_query_param = 'page_size'
#
#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'total': self.page.paginator.count,
#             'page': int(self.request.GET.get('page', DEFAULT_PAGE)), # can not set default = self.page
#             'page_size': int(self.request.GET.get('page_size', self.page_size)),
#             'results': data
#         })


# class CustomPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'count': self.page.paginator.count,
#             'page_size': self.page_size,
#             'results': data
#         })





