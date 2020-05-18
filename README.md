# A-BOWL-OF-DJANGO-TODO-LIST

> Django 한그릇 뚝딱 이라는 책 예제 중 TODO 리스트 따라하기



##### 목표

> 다른거 생각하지 않고, 책 내용에만 충실하기
> 예제 작성 후
>
> - 어떤 개념이과 연습이 부족한지 생각해보기
>
> - 다른 무엇을 확장해서 공부 해야 할지 생각해보기



##### 환경설정

> WSL에 환경 설정을 하고 윈도우에서 Pycharm을 통한 원격접속(?)을 통해 Django를 실행한다.
> [How install "pyenv" to Ubuntu on windows 10?](https://hihigash.com/how-install-pyenv-to-ubuntu-on-windows-adf48cc0577f)  -> 이건 세월이 많이 지나서... 파이썬 설치시 에러
>
> [Install Python 3.7.4 in pyenv on Ubuntu 18.04](https://mahdiech.com/posts/install-python-374-in-pyenv-on-ubuntu-1804/) :thumbsup:



- WSL에 pyenv 설치

```bash
# install pyenv requment libraries
sudo apt-get install \
    build-essential \
    libsqlite3-dev \
    sqlite3 \
    bzip2 \
    libbz2-dev \
    zlib1g-dev \
    libssl-dev \
    openssl \
    libgdbm-dev \
    libgdbm-compat-dev \
    liblzma-dev \
    libreadline-dev \
    libncursesw5-dev \
    libffi-dev \
    uuid-dev
```

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
```

```bash
# restart shell
exec $SHELL
```

- Django 3.0 버전대를 사용하기위해 파이썬 버전 3.8 버전대를 설치

  > [장고와 어떤 파이썬 버전을 사용해야 하나요?](https://docs.djangoproject.com/ko/3.0/faq/install/#what-python-version-can-i-use-with-django)
  >
  > Django 3버전대를 사용하기 위해서는 3.6 ~ 3.8 버전을 사용해야 함.
  >
  > 현재 시점 가장 높은 3.8.2 버전을 설치

  ```bash
  # you can check available versions
  pyenv install — list
  ```

  ```bash
  # install python
  pyenv install 3.8.2
  ```

  ```bash
  # set default version
  pyenv global 3.8.2
  ```

  ```bash
  # check using python version
  pyenv versions
  ```

  ```bash
  # or
  python — version
  ```

  

- vscode에서 wsl과 연동하여 파이썬 실행하기

  > [Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)
  > vscode 오피셜 개발 환경 셋팅 정보

  - 3줄 요약
    1. wsl을 설치한다.
    2. vscode를 설치한다.
    3. wsl을 통해 프로젝트 폴더로 가서 ```bash $>code .```을 실행한다.

  > 간단하지만 파이썬 파일을 만들자 마자 확장 플러그인들을 설치 유도하고
  >
  > 파이썬 파일을 터미널에서 바로 실행 할 수 있도록 했다. 굿!!
  >
  >
  > 또한 wsl 확장 플러그인 설치로 인해 기본 터미널을 wsl로 설정하고 사용하면 끝!!
  >
  > 엄청 간단하다.
  >
  > 속으로는 이게 여기서 끝나는 거 맞어?



##### 개발환경에 너무 욕심 부리지 말고 중요 기능에만 집중 하기!!

> 휴 또 다른 이상한거 막 찾아 볼뻔 했어.
>
> 그건 장고 환경을 구성하고 하나씩 잡아보자~



- WSL에서 장고 환경 구축하기

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

  - `pyenv`와 `vitualenv`를 활용한 가상 환경 구성하기

    - pyenv 설치

    - pyenv-virtualenv 설치

      ```bash
      $> git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
      $> echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
      $> source ~/.bashrc
      
      # 가상환경 만들기
      $> pyenv virtualenv 3.8.2 todo_list_env
      
      # 가상환경 삭제
      $> pyenv virtualenv-delete todo_list_env
      
      # 가상환경 구동!!
      $> pyenv activate todo_list_env
      
      # 구동 후 커맨드라인
      (todo_list_env) $> _
      
      ```

    - autoenv로 프로젝트 폴더 진입시마다 자동으로 환경설정

      ```bash
      # 설치
      $> git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
      
      # 원하는 폴더에 .env 파일을 만들고 스크립트를 적으면 자동 실행
      # 벗뜨 .env 파일은 다른곳에서도 사용되는 이름으로 .autoenv 같은
      # 다른 이름을 설정한다.
      
      # auto env 파일 이름을 자동에서 커스텀하게 설정
      # 주의! 'source ~/.autoenv/activate.sh' 설정 이전에 한다.
      $> echo 'export AUTOENV_ENV_FILENAME=".autoenv"' >> ~/.bashrc
      
      $> echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc
      ```

    - project 폴더에 .autoenv 파일을 만들고 아래에 다음과 같이 기입한다.

      ```bash
      echo "python pyenv > todo_list_env 진입"
      pyenv shell todo_list_env
      pyenv activate
      ```

    - 이제 프로젝트 폴더에 들어가면 아래와 같은 화면을 만나게 된다.
      y를 눌러준다.

      ```bash
      autoenv:
      autoenv: WARNING:
      autoenv: This is the first time you are about to source /mnt/e/projects/A-BOWL-OF-DJANGO-TODO-LIST/todo_list/.autoenv:
      autoenv:
      autoenv:   --- (begin contents) ---------------------------------------
      autoenv:     echo "python pyenv > todo_list_env M-lM-'M-^DM-lM-^^M-^E"$
      autoenv:     $
      autoenv:     pyenv shell todo_list_env$
      autoenv:     $
      autoenv:     pyenv activate$
      autoenv:
      autoenv:   --- (end contents) -----------------------------------------
      autoenv:
      autoenv: Are you sure you want to allow this? (y/N) y
      python pyenv > todo_list_env 진입
      pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.
      ```

- 장고 어플리케이션 시작(?)

  > ```bash
  > $> python -m pip install Django 
  > $> django-admin startproject todo_list
  > $> cd todo_list
  > $> python manage.py runserver
  > ```
  >
  > 이전에 프로젝트 생성 후 바로 실행했었다. 프로젝트 생성시 `todo_list`이름의 폴더가 생성되고 그안에 다시 `todo_list`이름의 폴더와 `manage.py`가 생성되었다.
  >
  >
  > 다른 책에서는 프로젝트 이름과 기본으로 생성된 폴더 이름이 동일한것이 혼동을 준다고 해서
  > 아래 `todo_list` 폴더를 다른 이름으로 변경 했던걸로 기억한다.
  >
  >
  > 우선 그대로 진행 해보자
  > 내부 `todo_list` 폴더중 setting.py 파일에 기본 생성된 설정 정보가 있으며
  >
  >
  > 더 자세히 보고 싶은 경우에는 파일 내부 상단 주석으로 처리된 공식 메뉴얼 정보를 참조하면 된다.
  >
  >
  > 하나의 프로젝트는 여러개의 `Application`으로 구성되며 아래와 같이 `manage.py`파일이 있는 곳에서 명령어를 실행하여 생성할 수 있다.
  >
  > ```bash
  > $> python manage.py startapp my_to_do_app
  > ```
  >
  > 새로 app 생성시 마다 
  > 프로젝트 폴더 > settings.py의 INSTALL_APPS 리스트에 app 이름을 추가해준다.
  >
  > ```python
  > ....
  > 
  > INSTALLED_APPS = [
  >     'django.contrib.admin',
  >     'django.contrib.auth',
  >     'django.contrib.contenttypes',
  >     'django.contrib.sessions',
  >     'django.contrib.messages',
  >     'django.contrib.staticfiles',
  >     'my_to_do_app\',
  > ]
  > ....
  > ```
