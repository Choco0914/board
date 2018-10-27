from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from post_service.forms import LoginForm
from .forms import JoinForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    """login을 하기위해 정의한다."""

    login_form = LoginForm()
    context = {'login_form':login_form,}

    return render(request, 'user_manager/login_form.html', context)

def login_validate(request):
    """로그인 결과값을 처리해준다"""
    login_form_data = LoginForm(request.POST)

    if login_form_data.is_valid():
        """form이 우리가 정의한 내용의 값과 일치한다. 로그인을 시도한다"""
        user = authenticate(username=login_form_data.cleaned_data['id'],
            password=login_form_data.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                auth_login(request, user)

                return redirect('/')
        else:
            return HttpResponse('사용자가 없거나 비밀번호를 잘못 눌렀습니다!')
    else:
        return HttpResponse('로그인 폼이 비정상적 입니다.')

    return HttpResponse('알 수 없는 오류 입니다.')

def join_page(request):
    """회원가입을 정의해준다"""
    if request.method == 'POST':
        join_form = JoinForm(request.POST)

        if join_form.is_valid():
            """문제가 없다면, 회원 가입 로직을 수행한다."""
            username = join_form.cleaned_data['id']
            password = join_form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)

            # 로그인 폼으로 이동시킨다.
            return redirect('/user/login')
    else:
        """만약 GET 등으로 넘어온 데이터이면 빈 FORM을 생성한다."""
        join_form = JoinForm()

    context = {'form':join_form}

    return render(request, 'user_manager/join_page.html', context)
