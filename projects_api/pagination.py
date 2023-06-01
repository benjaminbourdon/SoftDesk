from rest_framework.pagination import PageNumberPagination


class ListSetPagination(PageNumberPagination):
    page_size = 5
