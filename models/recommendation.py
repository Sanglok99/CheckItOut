from .topic_model import load_model

# 추천 로직을 담당하는 함수
def get_recommendations(user_input):
    model = load_model()
    topics, _ = model.transform([user_input])  # 사용자의 입력을 모델에 전달
    return topics  # 주제를 반환하거나, 관련 도서 추천 로직을 추가 가능