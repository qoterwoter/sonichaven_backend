from rest_framework import serializers
from .models import News, NewsArticle

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ('id', 'content', 'image', 'caption')

class NewsSerializer(serializers.ModelSerializer):
    article = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'created_at', 'updated_at', 'author', 'article')

    def get_article(self, obj):
        article = obj.articles.first() # assuming you want to get the first article
        if article:
            return NewsArticleSerializer(article).data
        else:
            return None

class NewsDetailSerializer(serializers.ModelSerializer):
    articles = NewsArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = News
        fields = ('id', 'title', 'created_at', 'updated_at', 'author', 'articles')
