from django.db import models
from django.utils import timezone
from django import forms
import re
from django.db.models import Q


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query



class Amostra(models.Model):

    Cliente = models.CharField(max_length=200)
    Cod_Amostra = models.CharField(max_length=10, null=True, blank=True)
    Valor = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    Data = models.DateField(default=timezone.now)
    Propriedade = models.CharField(max_length=200, null=True,blank=True)
    Gleba = models.CharField(max_length=200, null=True,blank=True)
    Municipio = models.CharField(max_length=200, null=True)
    GENDER_CHOICES = (
        ('MACRO', ' MACRONUTRIENTES (ROTINA)'),
        ('MICRONUTRIENTES', 'MICRONUTRIENTES (S, B, Fe, Cu, Mn, Zn)'),
        ('FISICA', 'ANALISE GRANULOMETRICA (FISICA)'),
        ('MICRO+MICRONUTRIENTES', 'MACRO+MICRONUTRIENTES (S, B, Fe, Cu, Mn, Zn)'),
        ('MACRO+MICRO+GRAN', 'MACRO+MICRO+GRANULOMETRICA(FISICA)'),
        ('ELEMENTOI', 'ELEMENTO ISOLADO (S, B)'),
        ('TECIDO', 'ANALISE DE TECIDO VEGETAL (COMPLETA)'),
        ('PH', 'pH ISOLADO (H2O , CaCl2)'),
    )
    Amostras = models.CharField(max_length=30, choices=GENDER_CHOICES, default='NAO SELECIONADO')
    Pago = models.BooleanField(default=False)





    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return  "Cliente: " + self.Cliente + "   Valor: R$" + str(self.Valor) + "   Data: " + str(self.Data) + "  Pago: " + str(self.Pago)


class Gasto(models.Model):

    Nome = models.CharField(max_length=200)
    Valor = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    Data = models.DateField(default=timezone.now)



    def __str__(self):
        return self.Nome + ",R$" + str(self.Valor)


def total(Amostra, Gasto):
    total = Amostra.Valor - Gasto.valor
    return total
