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
        }
        interfaces = (relay.Node, )
        
        

class Query(graphene.ObjectType):
    
    animeinfo = relay.Node.Field(Anime)
    all_animeinfo = DjangoFilterConnectionField(Anime)
    
    def resolve_animeinfo(self, info):
        return AnimeModel.objects.all()


schema = graphene.Schema(query=Query)