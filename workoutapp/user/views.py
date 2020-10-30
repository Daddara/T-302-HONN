from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

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
    follower_count = Follow.objects.filter(Following=user_info.user).count()
    is_following = Follow.objects.filter(Username=request.user)
    donation_form = Donate(initial={'amount': 100})
    request_user_wallet = Wallet.objects.get(user=request.user)
    sent_transactions = Transaction.objects.filter(sender=request.user)
    received_transactions = Transaction.objects.filter(receiver=request.user)

    user_is_following = []
    for follow_user in is_following:
        user_is_following.append(UserInfo.objects.get(user=follow_user.Following))

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
        'following': user_is_following,
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
            user_info.birth_date = form.cleaned_data['birth_date']
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
    # What the fck is poster?
    poster = Follow.objects.filter(Username=request.user)
    try:
        return render(request, 'user/followerlist.html', context={'follow': poster})
    except ValueError:
        return render(request, 'user/followerlist.html')


@login_required
def search_users(request):
    data = request.GET.get('search_input')
    if data:
        search_input = data
        # all users matching the query
        users = User.objects.filter(username__contains=search_input)
        if not users:
            return JsonResponse({}, status=204)

        # all users that the request user is already following
        request_user_following = Follow.objects.filter(Username=request.user)

        already_following = []
        # getting all the names and putting them in a list
        for user in request_user_following:
            already_following.append(user.Following.username)

        ret_list = []
        # for all users matching the search input check that they should be returned
        for user in users:
            if user.username != "System" and user.username != request.user.username \
                    and user.username not in already_following:
                users_info = UserInfo.objects.get(user=user)
                ret_list.append(users_info)

        # Creating an html string using template and some data
        html_response = render_to_string('user/follower_list.html', context={'users': ret_list})
        return HttpResponse(html_response, status=200)


@login_required
def follow(request):
    data = request.GET.get('user_id')
    try:
        user_id = int(data)
    except ValueError:
        return JsonResponse({'error': "Invalid request"}, status=400)

    try:
        follow_target = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': "Invalid request"}, status=400)

    user_following = Follow.objects.filter(Username=request.user)
    for already_following in user_following:
        if follow_target == already_following.Following:
            return JsonResponse({'msg': "Already following this user"}, status=200)

    new_following = Follow.objects.create(Username=request.user, Following=follow_target)
    return JsonResponse({'msg': "Successfully followed user"}, status=201)


@login_required
def new_friend_request(request, id):
    recipient = get_object_or_404(User, id=id)
    user_info = UserInfo.objects.get(user=recipient)
    friend_request, created = FriendRequest.objects.get_or_create(FromUser=request.user, ToUser=recipient)
    return redirect(user_info.get_abs_url())


@login_required
def unfriend(request, user_id):
    target = get_object_or_404(User, pk=user_id)
    request_user_info = get_object_or_404(UserInfo, user=request.user)
    target = get_object_or_404(UserInfo, user=target)
    target.friends.remove(request_user_info)
    request_user_info.friends.remove(target)
    return redirect('profile', slug=request.user.username)


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
