# 📄 Paper2Code Analysis - vLLM 실행 문제 해결 가이드

**⚠️ 주의: 이 저장소는 원본 Paper2Code 프로젝트의 실행 문제 해결을 위한 가이드입니다.**

## 🎯 개요

이 저장소는 [Paper2Code](https://github.com/going-doer/Paper2Code) 프로젝트의 **vLLM 실행 문제**를 해결하기 위한 가이드와 대안 방법을 제공합니다.

**중요**: 이 저장소는 원본 Paper2Code의 코드를 포함하고 있으며, 원본 프로젝트의 라이선스와 저작권을 준수합니다.

## ⚠️ 해결한 문제

- **PyTorch 버전 충돌**: vLLM 0.9.2와 현재 환경의 PyTorch 2.7.0a0 충돌
- **Kubernetes Pod 환경**: 기존 시스템에 크리티컬한 영향 방지
- **의존성 충돌**: numba, ray 등 여러 패키지 간 버전 충돌

## 📋 원본 Paper2Code 프로젝트 구조

원본 Paper2Code는 **두 가지 실행 방법**을 제공합니다:

### 1. OpenAI API 버전 (기존 기능)
```bash
# 원본 Paper2Code에서
cd scripts
bash run.sh  # ✅ OpenAI API 사용 - 이미 작동함
```

### 2. vLLM 버전 (새로운 기능)
```bash
# 원본 Paper2Code에서
cd scripts
bash run_llm.sh  # ❌ PyTorch 충돌로 실행 불가
```

## ✅ 해결 방안

### 방법 1: 원본 OpenAI API 버전 사용 (권장)
```bash
# 원본 Paper2Code 클론
git clone https://github.com/going-doer/Paper2Code.git
cd Paper2Code

# OpenAI API 키 설정
export OPENAI_API_KEY="your-api-key-here"

# 원본 실행
cd scripts
bash run.sh
```

### 방법 2: 가상환경에서 vLLM 설치 시도
```bash
# 가상환경 생성
python -m venv paper2code_env
source paper2code_env/bin/activate

# PyTorch 정식 버전 설치
pip install torch==2.7.0 torchvision==0.22.0 torchaudio==2.7.0 --index-url https://download.pytorch.org/whl/cu121

# vLLM 설치
pip install vllm

# 실행
cd scripts
bash run_llm.sh
```

## 🚀 빠른 시작

### 1. 원본 Paper2Code 사용 (권장)
```bash
git clone https://github.com/going-doer/Paper2Code.git
cd Paper2Code
export OPENAI_API_KEY="your-api-key-here"
cd scripts
bash run.sh
```

### 2. 이 저장소의 가이드 참조
```bash
git clone https://github.com/suhhongyiel/paper2code-analysis.git
cd paper2code-analysis
# README_ALTERNATIVE.md 참조
```

## 📁 이 저장소의 내용

이 저장소는 **원본 Paper2Code의 실행 문제 해결 가이드**를 제공합니다:

```
paper2code-analysis/
├── README.md                      # 이 파일 (가이드)
├── README_ALTERNATIVE.md          # 상세 문제 해결 가이드
├── SUMMARY.md                     # 문제 해결 과정 요약
├── codes/                         # 원본 Paper2Code 코드 (참고용)
├── scripts/                       # 원본 Paper2Code 스크립트 (참고용)
└── examples/                      # 원본 Paper2Code 예시 데이터
```

## 🔧 문제 해결 가이드

### 1. PyTorch 버전 충돌 해결
```bash
# 현재 PyTorch 버전 확인
python -c "import torch; print(torch.__version__)"

# 가상환경에서 정식 버전 설치
python -m venv env
source env/bin/activate
pip install torch==2.7.0 torchvision==0.22.0 torchaudio==2.7.0 --index-url https://download.pytorch.org/whl/cu121
```

### 2. vLLM 설치 문제 해결
```bash
# 의존성 충돌 확인
pip check

# vLLM 설치 시도
pip install vllm --no-deps
pip install ray[default] numba==0.61.2
```

### 3. 시스템 안전성 유지
```bash
# 가상환경 사용으로 시스템 격리
python -m venv isolated_env
source isolated_env/bin/activate
# 필요한 패키지만 설치
```

## 📊 원본 vs 해결책 비교

| 항목 | 원본 OpenAI API | 원본 vLLM | 해결책 |
|------|-----------------|-----------|--------|
| 설치 복잡도 | 🟢 낮음 | 🔴 높음 | 🟡 중간 |
| 시스템 영향 | 🟢 없음 | 🔴 높음 | 🟢 없음 |
| 실행 속도 | 🟡 중간 | 🟢 빠름 | 🟡 중간 |
| 코드 품질 | 🟢 높음 | 🟢 높음 | 🟢 높음 |
| 비용 | 🟡 있음 | 🟢 없음 | 🟡 있음 |
| 안정성 | 🟢 높음 | 🔴 낮음 | 🟢 높음 |

## 🎯 권장사항

### 1. **원본 Paper2Code의 OpenAI API 버전 사용** (가장 권장)
- ✅ 안정적이고 검증됨
- ✅ 시스템 영향 없음
- ✅ 완전한 기능 제공

### 2. **가상환경에서 vLLM 시도**
- ⚠️ 복잡하지만 무료
- ⚠️ 시스템 격리 필요

### 3. **이 저장소의 가이드 참조**
- 📚 문제 해결 방법 참고
- 📚 시스템 안전성 가이드

## 📄 저작권 및 라이선스

### 원본 프로젝트
- **Paper2Code**: [https://github.com/going-doer/Paper2Code](https://github.com/going-doer/Paper2Code)
- **라이선스**: Apache-2.0
- **저작권**: going-doer 및 Paper2Code 팀

### 이 저장소
- **목적**: 원본 Paper2Code의 실행 문제 해결 가이드
- **라이선스**: 원본 Paper2Code의 Apache-2.0 라이선스 준수
- **저작권**: 원본 코드는 going-doer 및 Paper2Code 팀 소유

### 사용 시 주의사항
1. **원본 프로젝트의 라이선스 준수 필수**
2. **상업적 사용 시 원본 프로젝트 라이선스 확인**
3. **저작권 표시 필수**
4. **이 저장소는 가이드 목적으로만 사용**

## 🙏 감사의 말

- [Paper2Code](https://github.com/going-doer/Paper2Code) 팀에게 감사드립니다.
- 원본 프로젝트의 라이선스와 저작권을 존중합니다.
- 이 저장소는 원본 프로젝트의 실행 문제 해결을 돕기 위한 것입니다.

## 📞 지원

### 원본 프로젝트 지원
- **Issues**: [Paper2Code Issues](https://github.com/going-doer/Paper2Code/issues)
- **Discussions**: [Paper2Code Discussions](https://github.com/going-doer/Paper2Code/discussions)

### 이 저장소 지원
- **목적**: 실행 문제 해결 가이드
- **범위**: PyTorch 충돌, 시스템 안전성 문제

---

**⚠️ 중요**: 이 저장소는 원본 Paper2Code 프로젝트의 실행 문제 해결을 위한 가이드입니다. 원본 프로젝트의 라이선스와 저작권을 반드시 준수해주세요.

**작업 완료**: 2024년 7월 21일  
**버전**: 1.0.0  
**상태**: 가이드 완성 