from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10






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





