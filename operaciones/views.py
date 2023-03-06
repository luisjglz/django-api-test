from fractions import Fraction
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

@method_decorator(csrf_exempt)
def my_view(request):
    if request.method == "GET":
        data = [{'num1': 5, 'den1': 3},{'num2': 8, 'den2': 7}]
        #return HttpResponse('hola mundo')
        return JsonResponse(data, safe=False)
        
    elif request.method == "POST":
        #return HttpResponse("respondiendo al post")
        data = json.loads(request.body)
        num1 = data['num1']
        den1 = data['den1']
        num2 = data['num2']
        den2 = data['den2']
        frac1 = Fraction(numerator=num1,denominator=den1)
        frac2 = Fraction(numerator=num2,denominator=den2)
        res = frac1 + frac2
        resstr = {"num":res.numerator, "den":res.denominator}
        return JsonResponse(resstr)

def di_adios(request):
    return HttpResponse('adios')


class Calculadora(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get (self, request):
        return HttpResponse("hola desde la calculadora")
    def post (self, request):
        """
        1. Leer los valores que vienen el post...
        2. Construir con esos valores 2 fracciones
        3. Restarlas
        4. Devolver el resultado como JSON con num & den
        """
        data = json.loads(request.body)
        frac1 = Fraction(numerator=data['num1'],denominator=data['den1'])
        frac2 = Fraction(numerator=data['num2'],denominator=data['den2'])
        res = frac1 - frac2
        resstr = {"num":res.numerator, "den":res.denominator}
        return JsonResponse(resstr)
