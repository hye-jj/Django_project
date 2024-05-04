from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def detail(request):
    # return HttpResponse('response detail')
    return render(request, 'index.html')


# Create your views here.
# def detail(request):
#     # return HttpResponse('reponse detail')
#     # return render(request, 'mvtapp/mvt_detail.html')
#     # return render(request, 'mvtapp/new_mvt_detail.html')

#     # request 인자 : http 패킷 전달. http 패킷 설정 :header,paybord, *세션(dstip, dst프로토콜)운반.
#     if request.method == 'POST':
#         title = request.POST.get('title')  # form 의 name - 변수명 request object 가 갖고있음.
#         count = request.POST.get('count')

#         # ORM 을 위한, 모델 오브젝트 생성
#         data = LectureDetail()
#         data.title = title
#         data.count = int(count)

#         data.save()

#         # after input, for review datas in DB
#         # objects 클래스명 static method : class 아래 method
#         # 일단 다 가져오는 편, 그러고 필터링하는 방법을 선호하심. - 개인의 차이
#         # datas = LectureDetail.objects.all()

#         #context 딕셔너리형태
#         # return render(request, 'mvtapp/new_mvt_detail.html', context={'datas':datas})  
#         return HttpResponseRedirect(reverse('mvtapp:detail'))
#         # Redirect POST 세션 끝남을 알림(세션 비워줌). - reverse(urls.py 의 패턴 name에 등록한 이름)

#     else:
#         datas = LectureDetail.objects.all()

#     return render(request, 'mvtapp/new_mvt_detail.html', context={'datas':datas})  