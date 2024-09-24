from django.shortcuts import render, redirect
from .models import Post

# Create your views here.


def add_post(request):

    if request.user.is_authenticated:
        if request.method == "POST":

            message = request.POST.get("message")

            message_length = 255

            if len(message) > message_length:
                context = {
                    "error":  "Message too long. exceed the limit",
                    "message": message[:message_length]
                }
                return render(request, "home.html", context)

            post = Post(message=message, user=request.user)
            post.save()

            return redirect("home")
