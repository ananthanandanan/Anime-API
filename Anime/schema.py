from  graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import AnimeModel
import graphene
        
        
class Anime(DjangoObjectType):
    class Meta:
        model = AnimeModel
        filter_fields = {
            'Name': ['exact', 'icontains', 'istartswith'],
            'Genre': ['in'],
            'Type': ['exact'],
            'Episode': ['gt', 'lt'],
            'Rating': ['gt', 'lt'],
            'Anime_id': ['exact'],
        }
        interfaces = (relay.Node, )
        
class AnimeType(DjangoObjectType):
    class Meta:
        model = AnimeModel
        fields = '__all__'

"""Defined what all data could be updated and taken as in input arguement"""
class AnimeInput(graphene.InputObjectType):
    id = graphene.Int()
    Name = graphene.String()
    Genre = graphene.String()
    Type = graphene.String()
    Episode = graphene.Int()
    Rating = graphene.Float()
    Members = graphene.Int()
        
class AnimeUpdate(graphene.Mutation):
    """ Input fields available"""
    class Arguments:
        id = graphene.Int(required=True)
        input = AnimeInput(required=True)
    """ Data that needs to be returned to the user for confirmation"""
    ok = graphene.Boolean()
    anime = graphene.Field(AnimeType)
    
    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        anime_instance = AnimeModel.objects.get(Anime_id=id)
        if anime_instance:
            ok = True
            anime_instance.Rating = input.Rating
            anime_instance.Episode = input.Episode
            anime_instance.save()
            return AnimeUpdate(ok=ok, anime=anime_instance)
        return AnimeUpdate(ok=ok, anime=None)
            
        
class Query(graphene.ObjectType):
    
    animeinfo = relay.Node.Field(Anime)
    all_animeinfo = DjangoFilterConnectionField(Anime)
    
    def resolve_animeinfo(self, info):
        return AnimeModel.objects.all()
    
class Mutation(graphene.ObjectType):
    animeupdate = AnimeUpdate.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)