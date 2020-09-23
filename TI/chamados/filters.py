import django_filters
from .models import Chamado

class FiltroChamado(django_filters.FilterSet):
	class Meta:
		model = Chamado
		fields = [ 'id','user', 'setor','relacao', 'situacao', 'problema']