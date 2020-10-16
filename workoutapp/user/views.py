from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from wallet.models import Wallet
from .forms.create_account_form import CreateAccountForm
from workout.models import Exercise
from .models import UserInfo, FriendRequest, Follow
from dashboard.views import add_like_information_to_exercises


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateAccountForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            new_user = User.objects.get(username=username)
            user_info = UserInfo.objects.create(user=new_user, slug=username)
            user_info.save()
            wallet = Wallet.objects.create(user=new_user)
            wallet.save()
            return redirect('login')

        return render(request, 'user/register.html', {
            'form': form, "errors": form.errors
        })

    return render(request, 'user/register.html', {
        'form': CreateAccountForm()
    })


@login_required
def profile_view(request, slug):
    request_user_info = UserInfo.objects.get(user=request.user)
    profile = UserInfo.objects.get(slug=slug)
    user = User.objects.get(username=profile)

    # Check if viewed user is logged in user's friend
    status = None
    if profile not in request_user_info.friends.all():
        status = 'not_friends'
        # Has a friend request been sent
        if len(FriendRequest.objects.filter(FromUser=request.user).filter(ToUser=user)) == 1:
            status = 'sent'

    exercise_models = None
    # If user is viewing own profile
    if request.user == user:

        try:
            exercise_models = Exercise.objects.filter(Creator=request.user)
            exercise_models = add_like_information_to_exercises(request, exercise_models)
        except Exercise.DoesNotExist:
            pass
    # Otherwise only get public exercises
    else:
        try:
            exercises = Exercise.objects.filter(Creator=user).filter(Public=True)
            exercise_models = add_like_information_to_exercises(request, exercise_models)
        except Exercise.DoesNotExist:
           pass

    context = {
        'user': user,
        'user_info': profile,
        'exercises': exercise_models,
        'status': status
    }
    return render(request, 'user/profile.html', context)

@login_required
def view_friend_and_requests(request):
    user = request.user
    user_info = UserInfo.objects.get(user=user)
    friends = user_info.friends.all()
    sent_requests = FriendRequest.objects.filter(FromUser=user)
    received_requests = FriendRequest.objects.filter(ToUser=user)
    return render(request, 'user/user_friends.html', context={'friends_list': friends,
                                                              'sent': sent_requests,
                                                              'received': received_requests})


@login_required
def following(request):
    poster = Follow.objects.filter(Username=request.user)
    try:
        return render(request, 'user/followerlist.html', context={'follow': poster})
    except ValueError:
        return render(request, 'user/followerlist.html')


@login_required
def delete_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, Creator=request.user, pk=exercise_id)
    exercise.delete()

    return redirect('profile', slug=request.user.username)


@login_required
def searchbarUsers(request):
    if request.method == 'GET':
        isFollowing = False
        search = request.GET.get('search')
        post = User.objects.all().filter(username=search)
        user = User.objects.get(username=request.user)
        followers = Follow.objects.all().filter(Username=request.user)
        for i in followers:
            for j in post:
                if i.Following.username == j.username:
                    isFollowing = True
        if post:
            return render(request, 'user/searchResults.html', context={'sr_user': post, 'current_user': user,
                                                                       'is_following': isFollowing})
        else:
            return render(request, 'user/searchResults.html')

    if request.method == 'POST':
        search = request.GET.get('search')
        post = User.objects.all().filter(username=search)
        poster = post.get(username=search)
        current_user = User.objects.get(username=request.user)
        follow = Follow(Username=current_user, Following=poster, FollowedAt="")
        follow.save()
        return redirect(following)


@login_required
def new_friend_request(request, id):
    recipient = get_object_or_404(User, id=id)
    user_info = UserInfo.objects.get(user=recipient)
    friend_request, created = FriendRequest.objects.get_or_create(FromUser=request.user, ToUser=recipient)
    return HttpResponseRedirect(user_info.get_abs_url())


@login_required
def cancel_friend_request(request, id):
    recipient = get_object_or_404(User, id=id)
    user_info = UserInfo.objects.get(user=recipient)
    friend_request = FriendRequest.objects.get(FromUser=request.user, ToUser=recipient)
    friend_request.delete()
    return HttpResponseRedirect(user_info.get_abs_url())


@login_required
def delete_friend_request(request, id):
    request_user = UserInfo.objects.get(user=request.user)
    sender = get_object_or_404(User, id=id)
    friend_request = FriendRequest.objects.get(FromUser=sender, ToUser=request.user)
    friend_request.delete()
    return HttpResponseRedirect(request_user.get_abs_url())


@login_required
def accept_friend_request(request, id):
    request_user = UserInfo.objects.get(user=request.user)
    sender = get_object_or_404(User, id=id)
    sender_info = UserInfo.objects.get(user=sender)
    friend_request = FriendRequest.objects.get(FromUser=sender, ToUser=request.user)
    receiver = friend_request.ToUser
    receiver_info = UserInfo.objects.get(user=receiver)
    sender_info.friends.add(receiver_info)
    receiver_info.friends.add(sender_info)
    friend_request.delete()
    return HttpResponseRedirect(request_user.get_abs_url())
