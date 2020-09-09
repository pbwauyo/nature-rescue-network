from django.shortcuts import render
from .models import CustomUser
from django.views import generic

class UsersListView(generic.ListView):
    template_name = 'account/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return CustomUser.objects.all()