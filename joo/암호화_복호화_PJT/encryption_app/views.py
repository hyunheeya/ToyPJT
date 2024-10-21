from django.shortcuts import render, redirect
from .models import Encryption, Decryption
from .forms import EncryptionForm, DecryptionForm
from django.contrib.auth.decorators import login_required

# 메인 페이지
def index(request):
    return render(request, 'encryption_app/index.html')

# 암호화 기능
@login_required
def encrypt(request):
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            data = {
                'content': form.cleaned_data['content'],
                'key': form.cleaned_data['key'],
            }
            shift = int(data['key'])
            encrypted = "".join([chr(ord(char) + shift) for char in data['content']])

            # 로그인한 사용자 확인
            if request.user.is_authenticated:
                encryption_instance = Encryption(
                    content=encrypted,
                    key=data['key'],
                    user=request.user  # 로그인한 사용자 설정
                )
                encryption_instance.save()

            # 결과를 템플릿에 전달
            return render(request, 'encryption_app/result.html', {'result': encrypted, 'key': data['key'], 'operation': 'Encryption'})
    else:
        form = EncryptionForm()
    return render(request, 'encryption_app/encrypt.html', {'form': form})




# 복호화 기능
@login_required
def decrypt(request):
    if request.method == 'POST':
        form = DecryptionForm(request.POST)
        if form.is_valid():
            # 폼의 클린 데이터 딕셔너리로 저장
            data = {
                'content': form.cleaned_data['content'],
                'key': form.cleaned_data['key'],
            }
            shift = int(data['key'])
            decrypted = "".join([chr(ord(char) - shift) for char in data['content']])

            # 복호화 결과를 전달하는 템플릿을 사용
            return render(request, 'encryption_app/decrypt_result.html', {'result': decrypted})
    else:
        form = DecryptionForm()

    # 폼이 유효하지 않거나 GET 요청일 경우 복호화 폼 템플릿을 반환
    return render(request, 'encryption_app/decrypt.html', {'form': form})


