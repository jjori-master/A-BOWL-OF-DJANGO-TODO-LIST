# A-BOWL-OF-DJANGO-TODO-LIST

> Django 한그릇 뚝딱 이라는 책 예제 중 TODO 리스트 따라하기



##### 목표

> 다른거 생각하지 않고, 책 내용에만 충실하기
> 예제 작성 후
>
> - 어떤 개념이과 연습이 부족한지 생각해보기
>
> - 다른 무엇을 확장해서 공부 해야 할지 생각해보기



##### 환경설정 (Windows)

- [Scoop 설치](https://github.com/jjori-master/pre-blog/blob/master/dev-env/%5B%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95%5D%20(%ED%95%84%EC%88%98)%20Scoop%20%EC%84%A4%EC%B9%98.md)

- [WSL 설치](https://github.com/jjori-master/pre-blog/blob/master/dev-env/%5B%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95%5D%20(%ED%95%84%EC%88%98)%20WSL%20%EC%84%A4%EC%B9%98.md)

- [Hyper 터미널 설치 및 설정](https://github.com/jjori-master/pre-blog/blob/master/dev-env/%5B%EC%83%9D%EC%82%B0%EC%84%B1%5D%20(%EC%84%A0%ED%83%9D)%20Hyper%20%ED%84%B0%EB%AF%B8%EB%84%90%20%EC%84%A4%EC%B9%98%20%EB%B0%8F%20%EC%84%A4%EC%A0%95.md)

- [pyenv 설치 및 설정](https://github.com/jjori-master/pre-blog/blob/master/dev-env/%5B%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD%5D%20(%ED%95%84%EC%88%98)%20pyenv%EB%A1%9C%20python%20%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95.md)

- [virtualenv 로 특정폴더(프로젝트) 가상환경 만들기](https://github.com/jjori-master/pre-blog/blob/master/dev-env/%5B%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD%5D%20(%ED%95%84%EC%88%98)%20Virtualenv%20%EB%A1%9C%20%ED%8A%B9%EC%A0%95%ED%8F%B4%EB%8D%94(%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8)%20%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD%20%EB%A7%8C%EB%93%A4%EA%B8%B0.md)

- [Autoenv로 프로젝트 폴더 진입시마다 자동으로 환경설정](https://github.com/jjori-master/pre-blog/blob/master/dev-env/%5B%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95%5D%20(%ED%95%84%EC%88%98)%20Autoenv%EB%A1%9C%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%ED%8F%B4%EB%8D%94%20%EC%A7%84%EC%9E%85%EC%8B%9C%EB%A7%88%EB%8B%A4%20%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C%20%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95.md)

  

##### 장고 환경 구축하기

> python 3버전 부터는 바늘에 실 가듯 `pip`이라는 패키지 매니저가 같이 딸려오는데
>
> 이것을 사용해서 Django 환경을 구축한다.

- [Django 공식 튜터리얼](https://docs.djangoproject.com/ko/3.0/intro/tutorial01/)로 이동해서 설치 방법을 확인한다.

  ```bash
  $> python -m pip install Django 
  $> django-admin startproject todo_list
  $> cd todo_list
  $> python manage.py runserver
  ```

- project 폴더에 .autoenv 파일을 만들고 아래에 다음과 같이 기입한다.

  ```bash
  echo "python pyenv > todo_list_env 진입"
  pyenv shell todo_list_env
  pyenv activate
  ```

- 장고 어플리케이션 시작(?)

  > ```bash
  > $> python -m pip install Django 
  > $> django-admin startproject todo_list
  > $> cd todo_list
  > $> python manage.py runserver
  > ```
  >
  > ```bash
  >$> python manage.py startapp my_to_do_app
  >```
  > 
  > 새로 app 생성시 마다 
  >프로젝트 폴더 > settings.py의 INSTALL_APPS 리스트에 app 이름을 추가해준다.
  >
  > ```python
  > ....
  >
  >INSTALLED_APPS = [
  > 'django.contrib.admin',
  > 'django.contrib.auth',
  > 'django.contrib.contenttypes',
  >  'django.contrib.sessions',
  > 'django.contrib.messages',
  >  'django.contrib.staticfiles',
  >  'my_to_do_app\',
  > ]
  >....
  > 
  > ```



###### 주의사항

- `Django can't redirect to the slash URL while maintaining POST data. `

  > [해당 내용 풀이](http://codingdojang.com/scode/377)
  > 장고의 `APPEND_SLASH`는 자동으로 URL 끝에 슬래시('/')를 붙여주는 옵션(Default=Ture)
  >
  > 위의 내용이 발생되는 원인은 Django가 urls.py 파일에 정의된 패턴과 일치하는 것이 없을때 자동으로 붙여서 다시 한번 일치하는지 확인하는데
  >
  > 일치하는 경우에는 슬래시를 붙인 url로 redirect가 일어난다.
  > 문제는 POST 요청일 경우 redirct가 발생되면 submit된 데이터가 유실될 수도 있기 때문에
  > 해당 오류가 발생된다.
  >
  > form에서 사용되는 url의 경우 끝에 슬래시('/')를 붙여준다.