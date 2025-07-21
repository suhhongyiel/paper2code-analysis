# 📄 Paper2Code Analysis - vLLM 대안 구현

Paper2Code 프로젝트의 vLLM 사용 부분을 기존 시스템에 영향을 주지 않고 재현한 대안 구현입니다.

## 🎯 개요

이 저장소는 [Paper2Code](https://github.com/going-doer/Paper2Code) 프로젝트의 vLLM 사용 부분을 PyTorch 버전 충돌 문제 없이 실행할 수 있도록 만든 대안 구현입니다.

## ⚠️ 해결한 문제

- **PyTorch 버전 충돌**: vLLM 0.9.2와 현재 환경의 PyTorch 2.7.0a0 충돌
- **Kubernetes Pod 환경**: 기존 시스템에 크리티컬한 영향 방지
- **의존성 충돌**: numba, ray 등 여러 패키지 간 버전 충돌

## ✅ 해결 방안

### 1. vLLM 대신 OpenAI API 사용
- 시스템 전역 환경에 영향 없음
- API 키 필요, 비용 발생 가능

### 2. Demo 모드 지원
- API 키 없이도 테스트 가능
- 기본적인 구조와 예시 코드 생성

## 🚀 빠른 시작

### 1. 저장소 클론
```bash
git clone https://github.com/suhhongyiel/paper2code-analysis.git
cd paper2code-analysis
```

### 2. Demo 모드 실행 (API 키 불필요)
```bash
cd scripts
bash run_alternative.sh
```

### 3. 실제 OpenAI API 사용
```bash
export OPENAI_API_KEY="your-api-key-here"
cd scripts
bash run_alternative.sh
```

## 📁 프로젝트 구조

```
p2c/
├── codes/                          # 핵심 구현 코드
│   ├── 1_planning_llm_alternative.py      # 계획 단계
│   ├── 2_analyzing_llm_alternative.py     # 분석 단계
│   ├── 3_coding_llm_alternative.py        # 코딩 단계
│   ├── 0_pdf_process.py                   # PDF 전처리
│   └── utils.py                           # 유틸리티 함수
├── scripts/                       # 실행 스크립트
│   └── run_alternative.sh                # 메인 실행 스크립트
├── examples/                      # 예시 데이터
│   ├── Transformer.json                  # Transformer 논문 JSON
│   └── Transformer_cleaned.json          # 전처리된 JSON
├── outputs/                       # 실행 결과 (자동 생성)
│   ├── Transformer_alternative/          # 분석 결과
│   └── Transformer_alternative_repo/     # 생성된 코드 저장소
├── README.md                      # 이 파일
├── README_ALTERNATIVE.md          # 상세 사용법
└── SUMMARY.md                     # 작업 요약
```

## 🔧 구현된 기능

### 1. 3단계 파이프라인
- **계획 단계**: 논문 분석 및 구현 계획 수립
- **분석 단계**: 기술적 분석 및 사양 정의
- **코딩 단계**: 실제 Python 코드 생성

### 2. Demo 모드
- API 키 없이도 전체 파이프라인 테스트 가능
- 기본적인 구조와 예시 코드 생성

### 3. 실제 API 모드
- OpenAI API를 사용한 고품질 분석 및 코드 생성
- 논문별 맞춤형 구현

## 📊 사용 시나리오

### 1. 빠른 테스트
```bash
# Demo 모드로 전체 파이프라인 테스트
bash scripts/run_alternative.sh
```

### 2. 실제 논문 구현
```bash
# OpenAI API 키 설정 후 실행
export OPENAI_API_KEY="your-key"
bash scripts/run_alternative.sh
```

### 3. 커스터마이징
```bash
# 개별 단계 실행
python codes/1_planning_llm_alternative.py \
  --paper_name "YourPaper" \
  --pdf_json_path "examples/YourPaper.json" \
  --output_dir "outputs/YourPaper"
```

## 🔍 결과 확인

### 생성된 분석 결과
```bash
# 계획 단계 결과
cat outputs/Transformer_alternative/planning_response.txt

# 분석 단계 결과
cat outputs/Transformer_alternative/analyzing_response.txt

# 코딩 단계 결과
cat outputs/Transformer_alternative/coding_response.txt
```

### 생성된 저장소
```bash
# 생성된 코드 확인
ls -la outputs/Transformer_alternative_repo/

# 메인 파일 실행
cd outputs/Transformer_alternative_repo
python test_demo.py
```

## 📈 성능 비교

| 항목 | 원본 vLLM | 대안 OpenAI API | Demo 모드 |
|------|-----------|-----------------|-----------|
| 설치 복잡도 | 🔴 높음 | 🟡 중간 | 🟢 낮음 |
| 시스템 영향 | 🔴 높음 | 🟢 없음 | 🟢 없음 |
| 실행 속도 | 🟢 빠름 | 🟡 중간 | 🟢 빠름 |
| 코드 품질 | 🟢 높음 | 🟢 높음 | 🟡 기본 |
| 비용 | 🟢 없음 | 🟡 있음 | 🟢 없음 |
| 안정성 | 🔴 낮음 | 🟢 높음 | 🟢 높음 |

## 🎉 성공 사례

### Transformer 논문 분석 완료
- ✅ 논문 내용 분석 및 계획 수립
- ✅ 기술적 사양 정의
- ✅ 기본 구현 코드 생성
- ✅ 완전한 프로젝트 구조 생성

### 시스템 안정성 유지
- ✅ 기존 PyTorch 설치 영향 없음
- ✅ Kubernetes Pod 환경 안전
- ✅ 의존성 충돌 완전 해결

## 🛠️ 문제 해결

### 1. 가상환경 사용 (권장)
```bash
python -m venv p2c_env
source p2c_env/bin/activate
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

## 📞 지원

문제가 발생하면 다음을 확인하세요:
1. Python 환경 설정
2. 필요한 패키지 설치 여부
3. API 키 설정 (실제 사용 시)
4. 파일 권한 설정

## 🔮 향후 개선 방향

1. **로컬 모델 지원**: 더 가벼운 로컬 모델 통합
2. **배치 처리**: 여러 논문 동시 처리
3. **템플릿 시스템**: 재사용 가능한 코드 템플릿
4. **품질 평가**: 생성된 코드의 품질 측정

## 📄 라이선스

이 프로젝트는 원본 [Paper2Code](https://github.com/going-doer/Paper2Code) 프로젝트의 대안 구현입니다.

## 🙏 감사의 말

- [Paper2Code](https://github.com/going-doer/Paper2Code) 팀에게 감사드립니다.
- OpenAI API를 활용한 대안 구현을 제공합니다.

---

**작업 완료**: 2024년 7월 21일  
**버전**: 1.0.0  
**상태**: ✅ 모든 테스트 통과 