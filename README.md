# Django_project

## 1. 실행 준비
- VSCODE 가상환경 설정 https://it4edu.tistory.com/160                                   
- VSCODE Django 패키지 설치 https://12716.tistory.com/entry/Django-%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-%EA%B8%B0%EB%B3%B8-%EC%84%B8%ED%8C%85VSCODE

### python venv 이용 가상환경 만들기
> python -m venv (환경이름)

- 인터프리터 설정(activate) :             
> F1 누르고 창에서 -> Python Select Interpreter             
> .\(환경이름)\Scripts\activate.bat  : activate.bat 파일 실행               
> 가상환경 폴더 밖에서 -> source 가상환경이름/Scripts/activate             
> 가상환경 안에서 C:/venv/Scripts/activation.bat (activation만 수행해도 됨)               

- 비활성화 : deactivate            

- 가상환경 삭제 : sudo rm -rf 가상환경이름 
               
<br>

## 2. 장고 start                 
가상환경폴더 안에서            
> pip install django             
                 
'./django_prj/scripts/python.exe -m pip install --upgrade pip'               

> pip install django-lint                

> django-admin startproject (mysite : 메인사이트이름)              
> cd mysite   # 폴더들어가기(manage.py 파일 있는곳)                  
> python manage.py runserver                  

<br>


## 3. 패키지 설치          
활성화된 가상 환경에서, pip install [패키지명] 명령어를 사용하여 패키지를 설치.          
- requirements.txt를 활용한 패키지 설치          
- requirements.txt 파일 내의 패키지를 한번에 모두 설치할 때는,            
  > pip install -r requirements.txt 
  
  명령어를 사용하여 패키지를 설치한다.            

<br>
                       
**가상 환경 내 패키지 리스트 확인 및 requirements.txt 만들기**     
- 가상환경 내 패키지 리스트 확인:    
  > pip freeze      
- 가상환경 내 패키지를 requirements.txt 만들기       
  > pip freeze > requirements.txt
- 가상환경 삭제하기       
  가상 환경은 결국 폴더 형태로 저장되기 때문에, 해당 폴더를 삭제하면 가상 환경도 함께 삭제된다.


