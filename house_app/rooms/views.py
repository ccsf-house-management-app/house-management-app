from django.shortcuts import render, redirect, get_object_or_404
from .models import RoomsAssign, Rooms
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from rest_framework import viewsets
from .serializers import RoomsAssignSerializer, RoomsSerializer, TenantRoomSerializer


class RoomsAssignView(viewsets.ModelViewSet):
    serializer_class = RoomsAssignSerializer
    queryset = RoomsAssign.objects.all()

class RoomsView(viewsets.ModelViewSet):
    serializer_class = RoomsSerializer
    queryset = Rooms.objects.all()

class TenantRoomView(viewsets.ModelViewSet):
    serializer_class = TenantRoomSerializer
    def get_queryset(self):
        queryset = RoomsAssign.objects.select_related('roomid').all()

class RoomListView(ListView):
    template_name = 'rooms/room_list.html'
    queryset= Rooms.objects.all()

class RoomAssignDetailView(DetailView):
    template_name = 'rooms/roominfo_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("tenantid")
        queryset = RoomsAssign.objects.select_related('roomid').get(id=id_)
        return get_object_or_404(RoomsAssign, tenantid=id_)



