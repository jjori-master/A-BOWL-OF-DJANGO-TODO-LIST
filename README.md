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





