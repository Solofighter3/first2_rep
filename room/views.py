from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from room.models import Room,Message

@login_required
def rooms(request):
    if "q" in request.GET:
        q=request.GET["q"]
        rooms=Room.objects.filter(name=q)
    else:
       rooms=Room.objects.all()
    return render(request,"rooms.html",{'rooms':rooms})

@login_required
def room(request,slug):
    room=Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=room)[0:25]
    print(messages)
    return render(request,"room.html",{'room':room,"messages":messages})


@login_required
def delete_todo(request,slug,id):
     Message.objects.filter(pk=id).delete()
     room=Room.objects.get(slug=slug)
     messages=Message.objects.filter(room=room)[0:25]
     return render(request,"room.html",{'room':room,"messages":messages})



