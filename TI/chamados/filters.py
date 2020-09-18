import django_filters
from .models import Chamado

class ChamadoFiltro(django_filters.FilterSet):
	class Meta:
		Model = Chamado
		fields = ('id', 'relacao', 'situacao')