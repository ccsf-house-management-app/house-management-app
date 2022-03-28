from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import UserInfoForm
from .models import UserInfo

class UserInfoListView(ListView):
    template_name = 'users/userinfo_list.html'
    queryset= UserInfo.objects.all()

class UserInfoDetailView(DetailView):
    template_name = 'users/userinfo_detail.html'
    queryset= UserInfo.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("userid")
        return get_object_or_404(UserInfo, userid=id_)

class UserInfoDetail(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userinfodetail.html', {})

def users(request):
    if request.user.is_authenticated:
        return render(request, 'users/users.html')
        # return render(request, 'users/userinfo_detail.html')
    else:
        return redirect('/users/signin')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/users')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/users')

        else:
            return render(request, 'users/signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'users/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('/users')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/users')
        else:
            form = AuthenticationForm()
            return render(request, 'users/signin.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'users/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/users/signin/')