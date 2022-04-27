from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from .models import RoomsAssign, Rooms, JoinRoom
from users.models import UserInfo
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from rest_framework import viewsets
from .serializers import RoomsAssignSerializer, RoomsSerializer, TenantRoomSerializer, JoinRoomSerializer


class RoomsAssignView(viewsets.ModelViewSet):
    serializer_class = RoomsAssignSerializer
    queryset = RoomsAssign.objects.all()

class RoomsView(viewsets.ModelViewSet):
    serializer_class = RoomsSerializer
    queryset = Rooms.objects.all()

class JoinRoomView(viewsets.ModelViewSet):
    queryset = JoinRoom.objects.raw('SELECT rooms_roomsassign.id, rooms_roomsassign.roomid_id, rooms_roomsassign.tenantid_id, rooms_roomsassign.date_start, rooms_roomsassign.date_end, rooms_roomsassign.date_transaction,rooms_roomsassign.transactionId, rooms_roomsassign.remarks, rooms_rooms.roomName, rooms_rooms.roomDescription, rooms_rooms.rent, rooms_rooms.capacity, rooms_rooms.date_created, users_userinfo.firstname, users_userinfo.lastname FROM rooms_roomsassign INNER JOIN rooms_rooms ON rooms_roomsassign.roomid_id = rooms_rooms.id INNER JOIN users_userinfo ON rooms_roomsassign.tenantid_id=users_userinfo.userid_id')
    serializer_class = JoinRoomSerializer

# class TenantRoomView(viewsets.ModelViewSet):
#     serializer_class = TenantRoomSerializer
#     def get_queryset(self):
#         queryset = RoomsAssign.objects.select_related('roomid').all()

# class TenantRoomView(viewsets.ViewSet):
#
#     def list(self, request):
#         tenantRoom = TenantRoom(
#             rooms=Rooms.objects.all(),
#             roomsassign=RoomsAssign.objects.all(),
#         )
#         serializer = TenantRoomSerializer(tenantRoom)
#         return Response(serializer.data)

class TenantRoomView(viewsets.ModelViewSet):
    queryset=RoomsAssign.objects.all()
    serializer_class=TenantRoomSerializer
    # process=Rooms.objects.all
    # serializer_class = RoomsAssignSerializer(process, many=True)

class RoomListView(ListView):
    template_name = 'rooms/room_list.html'
    queryset= Rooms.objects.all()

class RoomAssignDetailView(DetailView):
    template_name = 'rooms/roominfo_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("tenantid")
        queryset = RoomsAssign.objects.select_related('roomid').get(id=id_)
        return get_object_or_404(RoomsAssign, tenantid=id_)



