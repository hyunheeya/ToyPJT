# Encryptor Project

## 프로젝트 개요
이 프로젝트는 Django를 사용하여 단어를 암호화하고 복호화하는 웹 애플리케이션입니다. 사용자가 단어와 키를 입력하면 암호화된 결과를 출력하고, 암호화된 단어와 키를 입력하면 원래 단어를 복원할 수 있습니다.

## 기능
- **암호화**: 사용자가 입력한 단어를 키 값만큼 이동시켜 암호화된 단어를 생성합니다.
- **복호화**: 암호화된 단어와 키 값을 입력하면 원래 단어로 복원합니다.

## 기술 스택
- **프레임워크**: Django
- **언어**: Python, HTML
---
## 실행

- 메인 페이지 (로그인 x)
  
  <img width="563" alt="스크린샷 2024-10-20 오후 8 45 53" src="https://github.com/user-attachments/assets/a7fa9795-83e4-4a9d-860e-c8baf14e5c94">

- 메인 페이지 (로그인 o)
  
  <img width="564" alt="스크린샷 2024-10-20 오후 8 46 13" src="https://github.com/user-attachments/assets/2031b1c1-9fca-4500-8bbe-1757b80e395e">

- 암호화
  
   <img width="563" alt="스크린샷 2024-10-20 오후 8 46 26" src="https://github.com/user-attachments/assets/ed2ebbd4-c94e-4247-8133-cfdcb73b9177">

- 프로필 페이지

   <img width="562" alt="스크린샷 2024-10-20 오후 8 46 34" src="https://github.com/user-attachments/assets/555671e5-e0d2-4904-aa18-9cf3d9e49f1a">

- 복호화
  <img width="567" alt="스크린샷 2024-10-20 오후 9 09 10" src="https://github.com/user-attachments/assets/8b1cc460-962f-43ca-86aa-e9c8f0890318">

- 복호화 완료

   <img width="564" alt="스크린샷 2024-10-20 오후 8 46 53" src="https://github.com/user-attachments/assets/ae3d1813-3577-4f5d-81fc-4a43240a7c1d">
   
---

## 설치 및 실행 방법
1. 프로젝트 클론

```bash
git clone https://github.com/your-username/encryptor_project.git
cd encryptor_project
```

2. 가상 환경 생성 및 활성화

  ```python
  python -m venv venv
  source venv/bin/activate  # Windows에서는 venv\Scripts\activate
  ```
3. 패키지 설치

  ```python
  pip install -r requirements.txt
  ```
4. 마이그레이션 적용 및 서버 실행

  ```python
  python manage.py migrate
  python manage.py runserver
  ```

---
- 홈페이지: 암호화 및 복호화 기능을 선택할 수 있습니다.
- 암호화: 단어와 키를 입력하여 암호화된 결과를 확인할 수 있습니다.
- 복호화: 암호화된 단어와 키를 입력하여 원래 단어를 복원할 수 있습니다.

---

  
