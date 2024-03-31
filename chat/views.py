from django.shortcuts import render, redirect
from django.views import View
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Message, UserChannel
from django.db.models import Q


class Main(View):
    def get(self, request):
        # request.session['me_from_user'] =  'Hello me'
        # dta = {
        #         'type': 'receiver_func',
        #         'message': 'Hello from baby'
        #     }
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send('test', dta))

        if request.user.is_authenticated:
            return redirect("home")

        return render(request, "main.html")


class Home(View):
    def get(self, request):
        users = User.objects.all()
        if request.user.is_authenticated:
            context = {
                "user": request.user,
                "users": users,
            }
            return render(request, "home.html", context)
        return redirect("home")


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        data = request.POST.dict()
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request=request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect("home")

        context = {"error": "Data is wrong"}

        return render(request, "login.html", context)


class Register(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        context = {}

        data = request.POST.dict()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        try:
            new_user = User()
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.username = username
            new_user.email = email
            new_user.set_password(password)

            new_user.save()

            user = authenticate(request=request, username=username, password=password)

            if user != None:
                login(request, user)
                return redirect("home")
        except:
            context.update({"error": "Data is wrong"})

        return render(request, "register.html", context)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("main")


class ChatPerson(View):
    def get(self, request, pk):
        person = User.objects.get(id=pk)
        me = request.user
        messages = Message.objects.filter(
            Q(from_who=me, to_who=person) | Q(to_who=me, from_who=person)
        ).order_by("date", "time")

        user_channel_name = UserChannel.objects.get(user=person)
        data = {
            "type": "receiver_function",
            "type_of_data": "the_message_has_been_seen_from_other",
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)(user_channel_name.channel_name, data)

        message_have_not_been_seen = Message.objects.filter(
            from_who=person, to_who=me
        )
        message_have_not_been_seen.update(has_been_seen=True)

        context = {"person": person, "me": me, "messages": messages}
        return render(request, "chat_person.html", context)


# Create your views here.
