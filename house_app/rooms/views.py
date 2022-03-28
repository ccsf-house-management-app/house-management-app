from django.shortcuts import render, redirect, get_object_or_404
from .models import RoomsAssign, Rooms
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.

class RoomListView(ListView):
    template_name = 'rooms/room_list.html'
    queryset= Rooms.objects.all()

class RoomAssignDetailView(DetailView):
    template_name = 'rooms/roominfo_detail.html'
    queryset = RoomsAssign.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("tenantid")
        return get_object_or_404(RoomsAssign, tenantid=id_)