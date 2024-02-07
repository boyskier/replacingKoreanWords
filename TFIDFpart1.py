import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag

# nltk 리소스 다운로드 (처음 한 번만 실행 필요)
nltk.download('averaged_perceptron_tagger')


### 함수 정의 ###

# 한국어를 STOPWORD로 바꾸는 함수
def replace_korean_with_stopword(text):
    # 한국어 문자에 해당하는 regex 패턴
    pattern = re.compile('[\uAC00-\uD7A3]+')
    # 한국어 부분을 ' STOPWORD '로 대체 (앞뒤로 공백 추가)
    replaced_text = pattern.sub(' STOPWORD ', text)
    # 연속된 공백을 하나의 공백으로 축소
    cleaned_text = re.sub(r'\s+', ' ', replaced_text)
    return cleaned_text


def singularize_text(text, singularize_function):
    phrases = text.split('STOPWORD')  # 'STOPWORD'를 기준으로 텍스트를 분리
    singularized_phrases = []

    for phrase in phrases:
        # 각 phrase에 대해 singularize 함수 적용
        singularized_phrase = singularize_function(phrase.strip())
        singularized_phrases.append(singularized_phrase)

    # 'STOPWORD'를 사용하여 다시 합침
    return ' STOPWORD '.join(singularized_phrases)


# 기존에 제공된 singularize_last_word 함수
def singularize_last_word(phrase):
    lemmatizer = WordNetLemmatizer()
    parts = re.split(r'(\b-\b)', phrase)  # 하이픈을 별도의 부분으로 유지
    processed_parts = []
    for part in parts:
        if part != '-':  # 하이픈이 아닌 부분에 대해서만 처리
            words = part.split()
            if words:
                # 마지막 단어의 POS 태그 확인
                last_word = words[-1]
                pos_tag = nltk.pos_tag([last_word])[0][1]
                # 명사인 경우만 처리
                if pos_tag.startswith('N'):
                    words[-1] = lemmatizer.lemmatize(last_word, pos='n')
            processed_part = ' '.join(words)
            processed_parts.append(processed_part)
        else:
            processed_parts.append(part)  # 하이픈은 그대로 유지
    return ''.join(processed_parts)


### 실행 부분 ###

# 파일 읽어오기
englished_text_path = '해부학_15주차_강종순_1_englished.txt'
with open(englished_text_path, 'r', encoding='utf-8') as file:
    englished_text = file.read()

# 원본 텍스트 출력
print(englished_text)
print()
print('--------')
print()

# 한국어를 STOPWORD로 바꾼 텍스트 출력
replaced_korean_text = replace_korean_with_stopword(englished_text)
print(replaced_korean_text)

print()
print('--------')
print()

# singularize_last_word 함수를 사용하여 singularize된 텍스트 출력
singularized_text = singularize_text(replaced_korean_text, singularize_last_word)
print(singularized_text)
