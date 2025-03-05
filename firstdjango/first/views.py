from django.shortcuts import render


# 화면에 글씨를 출력하는 코드
def home(request):
    context = {"name": "이지수", "food": "샤브샤브", "name3": "아무개"}
    return render(request, "first/home.html", context)
