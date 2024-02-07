# 영한 혼합 텍스트 전처리 프로젝트

이 프로젝트는 영어와 한국어가 혼합된 텍스트를 전처리하기 위한 Python 스크립트를 제공합니다. 스크립트는 텍스트 내의 한국어 부분을 식별하여 * "STOPWORD" *로 대체하고, 남아 있는 영어 키워드들을 *단수형*으로 변환합니다.
이 프로젝트는 [AI_Lecturenote project](https://github.com/boyskier/AI_LectureNote_v1)에 포함됩니다.

# 목차

1. [프로젝트 소개](#프로젝트-소개)
2. [기능](#기능)
3. [요구 사항](#요구-사항)
4. [설치 방법](#설치-방법)
5. [사용 방법](#사용-방법)
6. [샘플 입력 및 출력](#샘플-입력-및-출력)
7. [함수 설명](#함수-설명)


## 기능

- **한국어 분리**: 자동으로 한국어 텍스트 부분을 식별하고 "STOPWORD"로 대체합니다.
- **영어 키워드 단수화**: 영어 키워드들을 기본형(단수형)으로 변환합니다.

## 요구 사항

- Python 3.x
- NLTK 라이브러리

## 설치 방법

스크립트를 실행하기 전에 Python과 NLTK가 설치되어 있는지 확인하세요. pip를 사용하여 NLTK를 설치할 수 있습니다:

```bash
pip install nltk
```

## 사용 방법

1. 영한 혼합 텍스트 파일을 스크립트와 같은 디렉토리에 위치시키세요. 파일은 UTF-8로 인코딩되어야 합니다.
2. 스크립트 내의 `englished_text_path` 변수를 당신의 텍스트 파일 이름과 일치하도록 수정하세요.
3. 스크립트를 실행하세요. 처리된 텍스트가 콘솔에 출력됩니다.

## 샘플 입력 및 출력

샘플 입력 및 출력은 당신이 직접 추가한다고 하셨으니, 처리 전과 후의 텍스트 예제를 명확하게 제공하세요. 예시는 다음과 같을 수 있습니다:

### 샘플 입력

`해부학_15주차_강종순_1_englished.txt`에서의 원본 텍스트:

```
오늘은 Cardiovascular development에 대해 중점적으로 알아보도록 하겠습니다. 심장은 전형적으로 4개의 atrium과 4개의 ventricle로 구성되어 있으며, arteries와 veins을 통해 혈류의 순환을 유지합니다.
```

### 샘플 출력

스크립트 실행 후:

```
STOPWORD Cardiovascular development STOPWORD  STOPWORD  STOPWORD  STOPWORD  STOPWORD . STOPWORD  STOPWORD 4 STOPWORD atrium STOPWORD 4 STOPWORD ventricle STOPWORD  STOPWORD  STOPWORD , artery STOPWORD vein STOPWORD  STOPWORD  STOPWORD  STOPWORD  STOPWORD .
```
development에 -> development STOPWORD로 한국어와 영어가 붙어 있는 경우, 한국어를 하나의 STOPWORD로 처리합니다. 

## 함수 설명

- `replace_korean_with_stopword(text)`: 한국어 텍스트 부분을 식별하여 "STOPWORD"로 대체합니다.
- `singularize_text(text, singularize_function)`: "STOPWORD" 플레이스홀더를 제외한 텍스트 내의 영어 키워드에 단수화 과정을 적용합니다.
- `singularize_last_word(phrase)`: 문구 내의 마지막 영어 키워드를 단수형으로 변환하는 보조 함수입니다.
