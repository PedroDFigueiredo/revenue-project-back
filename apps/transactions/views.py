# Create your views here.
from django.views.generic import TemplateView
from apps.transactions.models import Transaction


class TransactionsView(TemplateView):
	template_name = 'index.html'
	queryset = Transaction.objects.all()

	def get_context_data(self, **kwargs):
		p = kwargs
		p['transactions'] = self.queryset
		# etapa = VoleiEtapa.objects.get(id=32)
		# finalizaEtapa(etapa)

		return p

