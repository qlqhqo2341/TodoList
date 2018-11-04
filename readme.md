# TodoList 사용

## 개요
* 파이썬3 +  Django로 구현되어있습니다.
* TODO/settings.py에서 DB백엔드를 설정할 수 있습니다. 기본값은 SQLite입니다. (Django 기본 기능입니다.)

## 설치
* 파이썬3에서 `pip instal django`를 설치합니다.
    * 파이썬의 `virtualenv` 모듈로 가상환경에 설치할 수 있습니다.
* 터미널에서 `manage.py`파일이 존재하는 TODO폴더로 진입합니다.
* `python manage.py runserver`로 실행시켜서 서버를 구동시킵니다.
    * 아이피/포트 설정은 `python manage.py runserver 아이피:포트`입니다. 기본적으로 로컬호스트, 8000번 포트가 사용됩니다.