# TodoList

## 개요
* 파이썬3 +  Django로 구현되어있습니다.
* jquery, jquery ui, bootstrap 을 사용했습니다.

## 작동되는 기능
* 제목, 내용, 기한과 우선순위(중요, 우선, 일반)을 설정할 수 있습니다.
* 완료한 Todo에 체크표시를 할 수 있습니다.
* 완료하지 못하고 기한이 지난 TodoList는 알림을 표시합니다.
* 우선순위별로 Todo를 표시합니다.
* TodoList에서 우선순위 아이콘을 클릭하면 한 단계 상승합니다.
* 제목을 클릭하면 삭제,변경 아이콘과 내용을 볼 수 있습니다

## 설치
* 파이썬3에서 `pip instal django`를 설치합니다.
    * 파이썬의 `virtualenv` 모듈로 가상환경에 설치할 수 있습니다.
* 터미널에서 `manage.py`파일이 존재하는 TODO폴더로 진입합니다.
* TODO/settings.py에서 DB백엔드를 설정합니다. 기본적으로 SQLite를 사용하게 되어있습니다.
* db에 테이블을 만들기 위해서 `python manage.py makemigrates`와 `python manage.py migrate`를 시행합니다.
* `python manage.py runserver`로 실행시켜서 서버를 구동시킵니다.
    * 아이피/포트 설정은 `python manage.py runserver 아이피:포트`입니다. 기본적으로 로컬호스트, 8000번 포트가 사용됩니다.