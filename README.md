# OpsNow MCP Provider

## 소개
OpsNow MCP(Module Context Protocol) Provider는 OpsNow의 Cost MCP Server와 Asset MCP Server를 OpsNow API Bridge를 통해 연결하여 레거시 시스템과의 원활한 통신을 지원하는 프로젝트입니다.

## 시스템 구조
```mermaid
graph LR
    A[LLM Vendor Desktop App] --> |MCP Protocol| B[OpsNow MCP Server]
    B --> C[OpsNow MCP Provider]:::highlight
    C --> D[OpsNow Resources]
    
    classDef highlight fill:#2e8b57,stroke:#333,stroke-width:2px;
```

- **LLM Vendor Desktop App**: Claude와 같은 LLM 기반 데스크톱 애플리케이션
- **OpsNow MCP Server**: Asset 및 Cost 데이터를 MCP 형식으로 제공하는 서버
- **OpsNow MCP Provider**: OpsNow API Bridge를 통해 자원 데이터를 처리
- **OpsNow Resources**: 실제 OpsNow 리소스 데이터

## 현재 구현된 기능

- 기본 API 서버 구조
- 더미 데이터 기반의 자산 및 비용 정보 제공
- 헬스 체크 엔드포인트

## 기술 스택

- Python 3.8+
- FastAPI
- AsyncIO

## 설치 방법

1. Python 3.8 이상 설치
2. 의존성 패키지 설치:
```bash
pip install -r requirements.txt
```

3. 환경 설정:
```bash
cp .env.example .env
# .env 파일에 필요한 설정 입력
```

## 실행 방법

개발 서버 실행:
```bash
python main.py
```

프로덕션 서버 실행:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 환경 변수 설정

### 서버 설정
- `HOST`: 서버 호스트 주소 (기본값: 0.0.0.0)
- `PORT`: 서버 포트 (기본값: 8000)

### 로깅 설정
- `LOG_LEVEL`: 로깅 레벨 (DEBUG, INFO, WARNING, ERROR)
- `LOG_FORMAT`: 로그 포맷

## API 문서

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 모니터링

- Health Check: http://localhost:8000/health 