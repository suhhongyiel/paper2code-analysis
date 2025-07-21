# Paper2Code - vLLM 대안 구현

## 🎯 개요

Paper2Code 프로젝트의 vLLM 사용 부분을 기존 시스템에 영향을 주지 않고 재현한 대안 구현입니다.

## ⚠️ 문제 상황

- **PyTorch 버전 충돌**: 현재 환경의 PyTorch 2.7.0a0와 vLLM 요구사항 충돌
- **Kubernetes Pod 환경**: 기존 시스템에 크리티컬한 영향 방지 필요
- **의존성 충돌**: 여러 패키지 간 버전 충돌

## ✅ 해결 방안

### 1. vLLM 대신 OpenAI API 사용
- **장점**: 시스템 전역 환경에 영향 없음
- **단점**: API 키 필요, 비용 발생 가능

### 2. Demo 모드 지원
- **장점**: API 키 없이도 테스트 가능
- **기능**: 기본적인 구조와 예시 코드 생성

## 🚀 사용 방법

### 1. 가상환경에서 실행 (권장)

```bash
# 가상환경 활성화
source vllm_env/bin/activate

# 필요한 패키지 설치
pip install openai transformers tiktoken

# 대안 스크립트 실행
cd scripts
bash run_alternative.sh
```

### 2. Demo 모드 실행

```bash
# API 키 없이 실행 (Demo 모드)
cd scripts
bash run_alternative.sh
```

### 3. 실제 OpenAI API 사용

```bash
# 환경 변수 설정
export OPENAI_API_KEY="your-api-key-here"

# 스크립트 실행
cd scripts
bash run_alternative.sh
```

## 📁 생성된 파일 구조

```
outputs/
├── Transformer_alternative/
│   ├── planning_response.txt      # 계획 단계 결과
│   ├── analyzing_response.txt     # 분석 단계 결과
│   └── coding_response.txt        # 코딩 단계 결과
└── Transformer_alternative_repo/  # 최종 코드 저장소
    ├── main.py                    # 메인 실행 파일
    ├── config.yaml               # 설정 파일
    ├── requirements.txt          # 의존성 목록
    └── README.md                 # 사용법 설명
```

## 🔧 구현된 스크립트

### 1. `1_planning_llm_alternative.py`
- **기능**: 논문 분석 및 구현 계획 수립
- **입력**: 논문 JSON/LaTeX 파일
- **출력**: 상세한 구현 계획

### 2. `2_analyzing_llm_alternative.py`
- **기능**: 논문의 기술적 분석
- **입력**: 논문 내용
- **출력**: 구현 사양서

### 3. `3_coding_llm_alternative.py`
- **기능**: 실제 코드 생성
- **입력**: 분석 결과
- **출력**: 완전한 Python 구현

## 📊 Demo 모드 vs 실제 API

### Demo 모드
- ✅ **즉시 실행 가능**
- ✅ **API 키 불필요**
- ✅ **비용 없음**
- ⚠️ **기본적인 예시 코드만 생성**

### 실제 OpenAI API
- ✅ **고품질 분석 및 코드 생성**
- ✅ **논문별 맞춤형 구현**
- ⚠️ **API 키 필요**
- ⚠️ **비용 발생 가능**

## 🎯 사용 시나리오

### 1. 빠른 테스트
```bash
# Demo 모드로 전체 파이프라인 테스트
bash run_alternative.sh
```

### 2. 실제 논문 구현
```bash
# OpenAI API 키 설정 후 실행
export OPENAI_API_KEY="your-key"
bash run_alternative.sh
```

### 3. 커스터마이징
```bash
# 개별 단계 실행
python ../codes/1_planning_llm_alternative.py \
  --paper_name "YourPaper" \
  --pdf_json_path "../examples/YourPaper.json" \
  --output_dir "../outputs/YourPaper"
```

## 🔍 결과 확인

### 1. 계획 단계 결과
```bash
cat ../outputs/Transformer_alternative/planning_response.txt
```

### 2. 분석 단계 결과
```bash
cat ../outputs/Transformer_alternative/analyzing_response.txt
```

### 3. 생성된 코드
```bash
cat ../outputs/Transformer_alternative_repo/main.py
```

### 4. 전체 저장소 구조
```bash
tree ../outputs/Transformer_alternative_repo/
```

## 🛠️ 문제 해결

### 1. 가상환경 문제
```bash
# 가상환경 재생성
python -m venv new_vllm_env
source new_vllm_env/bin/activate
pip install openai transformers tiktoken
```

### 2. API 키 문제
```bash
# API 키 확인
echo $OPENAI_API_KEY

# API 키 설정
export OPENAI_API_KEY="your-key-here"
```

### 3. 권한 문제
```bash
# 실행 권한 부여
chmod +x scripts/run_alternative.sh
```

## 📈 성능 비교

| 항목 | vLLM (원본) | OpenAI API (대안) | Demo 모드 |
|------|-------------|-------------------|-----------|
| 설치 복잡도 | 높음 | 낮음 | 없음 |
| 실행 속도 | 빠름 | 중간 | 빠름 |
| 코드 품질 | 높음 | 높음 | 기본 |
| 시스템 영향 | 높음 | 없음 | 없음 |
| 비용 | 없음 | 있음 | 없음 |

## 🎉 성공 사례

✅ **Transformer 논문 분석 완료**
- 계획 단계: 구현 로드맵 생성
- 분석 단계: 기술적 사양 정의
- 코딩 단계: 기본 구현 코드 생성

✅ **시스템 안정성 유지**
- 기존 PyTorch 설치 영향 없음
- Kubernetes Pod 환경 안전
- 의존성 충돌 해결

## 🔮 향후 개선 방향

1. **로컬 모델 지원**: 더 가벼운 로컬 모델 통합
2. **배치 처리**: 여러 논문 동시 처리
3. **템플릿 시스템**: 재사용 가능한 코드 템플릿
4. **품질 평가**: 생성된 코드의 품질 측정

## 📞 지원

문제가 발생하면 다음을 확인하세요:
1. 가상환경 활성화 상태
2. 필요한 패키지 설치 여부
3. API 키 설정 (실제 사용 시)
4. 파일 권한 설정

---

**참고**: 이 대안 구현은 원본 Paper2Code의 기능을 유지하면서 시스템 호환성 문제를 해결합니다. 