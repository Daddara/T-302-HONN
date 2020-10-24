from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from wallet.models import Wallet, Transaction
from .forms.create_account_form import CreateAccountForm
from workout.models import Exercise
from workout.models import Workout
from .forms.donate_form import Donate
from .models import UserInfo, FriendRequest, Follow
from dashboard.views import add_like_information_to_exercises
from dashboard.views import add_like_information_to_workouts
from user.forms.create_account_form import EditUserInfoForm


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
    user_info = UserInfo.objects.get(slug=slug)
    user = User.objects.get(username=user_info)
    friends = user_info.friends.all()
    sent_requests = FriendRequest.objects.filter(FromUser=user)
    received_requests = FriendRequest.objects.filter(ToUser=user)
    follower_count = Follow.objects.filter(Following=request.user).count()
    is_following = Follow.objects.filter(Username=request.user)
    donation_form = Donate(initial={'amount': 100})
    request_user_wallet = Wallet.objects.get(user=request.user)
    sent_transactions = Transaction.objects.filter(sender=request.user)
    received_transactions = Transaction.objects.filter(receiver=request.user)
    print(sent_transactions)
    print(received_transactions)

    # Check if viewed user is logged in user's friend
    status = None
    if user_info not in request_user_info.friends.all():
        status = 'not_friends'
        # Has a friend request been sent
        if len(FriendRequest.objects.filter(FromUser=request.user).filter(ToUser=user)) == 1:
            status = 'sent'
        elif len(FriendRequest.objects.filter(FromUser=user).filter(ToUser=request.user)) == 1:
            status = 'received'

    # If user is viewing own user_info
    if request.user == user:
        try:
            exercise_models = Exercise.objects.filter(Creator=request.user)
            exercise_models = add_like_information_to_exercises(request, exercise_models)

        except Exercise.DoesNotExist or Workout.DoesNotExist:
            exercise_models = None

        try:
            workout_models = Workout.objects.filter(User=request.user)
            workout_models = add_like_information_to_workouts(request, workout_models)
        except Workout.DoesNotExist:
            workout_models = None

    # Otherwise only get the slug's public exercises
    else:
        if request.method == "POST":
            donation_form = Donate(data=request.POST)
            # someone tryna donate this bitch niga
            if donation_form.is_valid():
                # Check if oke and transfa da liras
                amount = donation_form.cleaned_data['amount']
                if request_user_wallet.fitcoin < amount:
                    donation_form.add_error('amount', "Insufficient funds for transaction!")
                else:
                    donation_target = get_object_or_404(User, username=slug)
                    target_user_wallet = Wallet.objects.get(user=donation_target)
                    target_user_wallet.add_balance(amount)
                    request_user_wallet.remove_balance(amount)
                    new_transaction = Transaction.objects.create(sender=request.user, receiver=donation_target,
                                                                 amount=amount)
                    new_transaction.save()
                    donation_form = Donate(initial={'amount': 100})
                    messages.add_message(request, messages.SUCCESS, 'Donation sent!')
            else:
                # Sumting wong
                donation_form.add_error(None, "Something went terribly wrong!")

        try:
            exercise_models = Exercise.objects.filter(Creator=user).filter(Public=True)
            exercise_models = add_like_information_to_exercises(request, exercise_models)
        except Exercise.DoesNotExist:
            exercise_models = None

        try:
            workout_models = Workout.objects.filter(User=user)
            workout_models = add_like_information_to_workouts(request, workout_models)
        except Workout.DoesNotExist:
            workout_models = None

    context = {
        'user': user,
        'user_info': user_info,
        'exercises': exercise_models,
        'workouts': workout_models,
        'status': status,
        'friends': friends,
        'sent_requests': sent_requests,
        'received_requests': received_requests,
        'follower_count': follower_count,
        'following': is_following,
        'donation_form': donation_form,
        'user_wallet': request_user_wallet,
        'sent_transactions': sent_transactions,
        'received_transactions': received_transactions
    }

    return render(request, 'user/profile.html', context)


@login_required
def edit_profile_view(request):
    # User info instance of user
    user_info = UserInfo.objects.get(user=request.user)
    # If the request is to edit user info
    if request.method == 'POST':
        form = EditUserInfoForm(request.POST)
        if form.is_valid():
            user_info.age = form.cleaned_data['age']
            user_info.first_name = form.cleaned_data['first_name']
            user_info.last_name = form.cleaned_data['last_name']
            user_info.bio = form.cleaned_data['bio']
            user_info.email = form.cleaned_data['email']
            user_info.profile_image = form.cleaned_data['profile_image']
            user_info.cover_image = form.cleaned_data['cover_image']
            user_info.save()
            return redirect('profile', slug=request.user.username)

    # If the request is to get user info / Or the user info was incorrect on submission
    form = EditUserInfoForm(instance=user_info)
    return render(request, 'user/edit_profile.html', {'form': form})


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
def searchbarUsers(request):
    if request.method == 'GET':
        isFollowing = False
        search = request.GET.get('search')
        if not search:
            search = ""
        post = User.objects.filter(username__contains=search)
        user = User.objects.get(username=request.user)
        followers = Follow.objects.filter(Username=request.user)
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
        post = User.objects.filter(username__contains=search)
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
    return redirect(user_info.get_abs_url())


@login_required
def cancel_friend_request(request, id):
    recipient = get_object_or_404(User, id=id)
    user_info = UserInfo.objects.get(user=recipient)
    friend_request = FriendRequest.objects.get(FromUser=request.user, ToUser=recipient)
    friend_request.delete()
    return redirect('profile', slug=request.user.username)


@login_required
def delete_friend_request(request, id):
    request_user = UserInfo.objects.get(user=request.user)
    sender = get_object_or_404(User, id=id)
    friend_request = FriendRequest.objects.get(FromUser=sender, ToUser=request.user)
    friend_request.delete()
    return redirect('profile', slug=request.user.username)


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
    return redirect('profile', slug=request.user.username)
