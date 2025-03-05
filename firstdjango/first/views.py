from django.shortcuts import render


# 화면에 글씨를 출력하는 코드
def home(request):
    context = {"name": "이지수", "interest": "샤브샤브", "hobby": "아무개"}
    return render(request, "first/home.html", context)
