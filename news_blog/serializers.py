from rest_framework import serializers
from .models import News, NewsArticle

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ('id', 'content', 'image', 'caption')

class NewsSerializer(serializers.ModelSerializer):
    articles = NewsArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = News
        fields = ('id', 'title', 'created_at', 'updated_at', 'author', 'articles')
