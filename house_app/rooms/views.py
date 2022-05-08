from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Sum, Count, F, Window
from .models import RoomsAssign, Rooms, JoinRoom, MonthlyTenant
from users.models import UserInfo
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from rest_framework import viewsets
from .serializers import RoomsAssignSerializer, RoomsSerializer, TenantRoomSerializer, JoinRoomSerializer, MonthlyTenantSerializer


class RoomsAssignView(viewsets.ModelViewSet):
    serializer_class = RoomsAssignSerializer
    queryset = RoomsAssign.objects.all()


class RoomsView(viewsets.ModelViewSet):
    serializer_class = RoomsSerializer
    queryset = Rooms.objects.all()


class JoinRoomView(viewsets.ModelViewSet):
    queryset = JoinRoom.objects.raw('SELECT rooms_roomsassign.id, rooms_roomsassign.roomid_id, rooms_roomsassign.tenantid_id, rooms_roomsassign.date_start, rooms_roomsassign.date_end, rooms_roomsassign.date_transaction,rooms_roomsassign.transactionId, rooms_roomsassign.remarks, rooms_rooms.roomName, rooms_rooms.roomDescription, rooms_rooms.rent, rooms_rooms.capacity, rooms_rooms.date_created, users_userinfo.firstname, users_userinfo.lastname FROM rooms_roomsassign INNER JOIN rooms_rooms ON rooms_roomsassign.roomid_id = rooms_rooms.id INNER JOIN users_userinfo ON rooms_roomsassign.tenantid_id=users_userinfo.userid_id')
    serializer_class = JoinRoomSerializer

class MonthlyTenantView(viewsets.ModelViewSet):
    serializer_class = MonthlyTenantSerializer
    queryset = MonthlyTenant.objects.raw('Select id, formonth, foryear, tenants, (@csum := @csum + tenants) as monthly_tenants from ( SELECT rooms_roomsassign.id AS id, COUNT(DISTINCT(rooms_roomsassign.tenantid_id)) AS tenants, rooms_roomsassign.formonth AS formonth, rooms_roomsassign.foryear AS foryear FROM rooms_roomsassign WHERE rooms_roomsassign.date_end IS NULL GROUP BY rooms_roomsassign.formonth, rooms_roomsassign.foryear ) As temp JOIN (SELECT @csum:=0) AS temp2')


class TenantRoomView(viewsets.ModelViewSet):
    queryset=RoomsAssign.objects.all()
    serializer_class=TenantRoomSerializer

class RoomListView(ListView):
    template_name = 'rooms/room_list.html'
    queryset= Rooms.objects.all()

class RoomAssignDetailView(DetailView):
    template_name = 'rooms/roominfo_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("tenantid")
        queryset = RoomsAssign.objects.select_related('roomid').get(id=id_)
        return get_object_or_404(RoomsAssign, tenantid=id_)



