import graphene
from graphene_django import DjangoObjectType

from project.polls.models import Poll, Question


class PollType(DjangoObjectType):
    class Meta:
        model = Poll
        fields = ('id', 'name', 'questions',)


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('id', 'text', 'poll')


class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    poll_by_name = graphene.Field(PollType, name=graphene.String(required=True))

    def resolve_all_questions(root, info):
        return Question.objects.select_related('poll').all()
    
    def resolve_poll_by_name(root, info, name):
        try:
            return Poll.objects.get(name=name)
        except Poll.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)