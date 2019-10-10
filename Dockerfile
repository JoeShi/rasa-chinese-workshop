FROM rasa/rasa:latest-full

WORKDIR /app

COPY requirements.txt /app
COPY data/total_word_feature_extractor_zh.dat /app/data/

ENTRYPOINT ["rasa"]