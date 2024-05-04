## TDD 과목개요
웹서비스를 TDD 프로세스에 따라 효과적으로 코드를 작성하는 것을 목표로 함.

- 이를 위해 Django 웹서비스 프레임워크 이용.


### TDD 란?
- 테스트주도개발, 1999년도 XP(Extreme Programming)라는 애자일 기반 개발 방법론에서 소개.
- 짧은 주기의 반복에 의존하는 개발 프로세스로 XP의 "Test-First" 개념에 기반을 둔 단순한 설계 중시.
- '프로그램을 작성하기 전에 테스트를 먼저 작성하는 것' - 켄트 벡
- 단위 테스트를 활용하여 보다 높은 수준의 코드 품질을 확보.
- **개발 하기 전에 테스트 코드를 먼저 작성**
- 매소드 및 모듈을 작성하기 전에 작성 종료 조건을 먼저 정해놓고 코딩을 시작함.

### RED-GREEN-REFACTOR 
TDD를 가장 쉽게 표현한 것이  RED-GREEN-REFACTOR 개발 주기  

![TDD](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwm9o6uROkDxaS-PzKKXkTWV3jDc7Zz9wnkLUvpbt9-Q&s)    

### 기존 개발 방식과 차이
**기존 개발 방식**             
구현 > 웹브라우저로 확인 > 성공 > 개선점찾기

:white_check_mark: 만들고 싶은 요소를 떠올리고 우선 개발      
:white_check_mark: 웹 브라우저로 결과 확인        
:white_check_mark: 제대로 동작하지 않으면 다시 개발            
:white_check_mark: 성공하면 개선점 찾기                   
             
**TDD: Test Driven Development**         
테스트 코드 작성 > 기능 구현 > 리팩토링         
          
1. 테스트 코드 작성         
:white_check_mark: 만들고 싶은 기능 점검할 코드 작성          
:white_check_mark: 아직 기능을 구현하지 않았으므로 테스트 당연히 실패              
              
2. 기능 구현           
:white_check_mark: 테스트 코드를 만족시키도록 기능 구현      
:white_check_mark: 테스트 통과를 최우선 목표로 작업        
                  
3. 리팩토링            
:white_check_mark: 기능의 성능을 향상시키거나, 재사용성이 좋거나, 가독성이 좋은 코드로 개선        
:white_check_mark: 테스트 코드로 다시 기능을 점검        
             
             

<br>


## Django 간단 테스트
**python manage.py test**
            
![alt text](./myblog/django%20test.png)


