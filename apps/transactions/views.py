from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from apps.transactions.models import Transaction


class TransactionsView(ListView):
	template_name = 'index.html'
	queryset = Transaction.objects.all()

	def get_context_data(self, **kwargs):
		p = kwargs
		p['transactions'] = self.queryset
		# etapa = VoleiEtapa.objects.get(id=32)
		# finalizaEtapa(etapa)

		return p
