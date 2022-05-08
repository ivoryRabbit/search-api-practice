# Search API

### 개발 환경
1. [docker](https://hub.docker.com/search?type=edition&offering=community&q=) 설치
2. docker 실행
   - `docker-compose -f docker-compose.yml up --build`
3. 아래 로그가 뜨면 실행 완료
   - `search-api | INFO: Application startup complete.`
4. swagger 접속 확인
   - http://0.0.0.0:8000/docs

### API 테스트
- 터미널에서 다음 명령 실행
  ```bash
  curl -G -v "http://localhost:8000/search" --data-urlencode "query=star"
  ```
- 혹은 브라우저에서 다음 url로 접속
  - http://localhost:8000/search?query=star
- 혹은 swagger에서 `try it out` 클릭

### 데이터 확인용 개발 환경
1. `pip3 install -r requirements.txt`
2. `export PYTHONPATH=$(pwd)`
3. `python3 app/batch/load_data.py`
4. `python3 app/batch/build_tokenized_text.py`
5. `python3 app/batch/build_inverted_index.py`
6. `uvicorn app.main:app --reload`