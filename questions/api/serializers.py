from rest_framework import serializers
from questions.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]

    def get_created_at(self, Question):
        return Question.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, Question):
        return Question.voters.count()

    def get_user_has_voted(self, Question):
        request = self.context.get("request")
        return Question.voters.filter(pk=request.user.pk).exists()

    def get_question_slug(self, Question):
        return Question.question.slug


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_created_at(self, Question):
        print(type(Question))
        return Question.created_at.strftime("%B %d, %Y")

    def get_answers_count(self, Question):
        return Question.answers.count()

    def get_user_has_answered(self, Question):
        request = self.context.get("request")
        print(Question.answers.filter(author=request.user).exists())
        return Question.answers.filter(author=request.user).exists()
