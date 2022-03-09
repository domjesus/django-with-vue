from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ContatoSerializer


# @login_required(redirect_field_name='login')
def index(request):
    # messages.add_message(request, messages.ERROR, "Ocorreu um erro!")

    contatos = Contato.objects.order_by('-id').filter(
        show_on_list=True
    )
    # dir(contatos)
    # print(contatos)
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    context = {'contatos': contatos}
    return render(request, 'contatos/index.html', context)


def show(request, id):

    contato = get_object_or_404(Contato, id=id)

    if not contato.show_on_list:
        raise Http404()

    # contato = Contato.objects.get(id=id)
    # print(request, contato)
    # context = {'contatos': contato}
    return render(request, 'contatos/show.html', {'contato': contato})
    # except Contato.DoesNotExist as e:
    #     raise Http404()


def search(request):
    print(dir(request))
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR,
                             "O termo deve ser preenchido")
        messages.add_message(request, messages.SUCCESS, "Irra")
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        show_on_list=True,
    )
    # contatos = Contato.objects.filter(
    #     Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
    #     show_on_list=True,
    # )
    # print(contatos.query)
    # dir(contatos)
    # print(contatos)
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    context = {'contatos': contatos}
    return render(request, 'contatos/index.html', context)


@csrf_exempt
def list_contatos(request):
    if(request.method == 'GET'):
        contatos = Contato.objects.all()

        serializer = ContatoSerializer(contatos, many=True)

        return JsonResponse(serializer.data, safe=False)

    # return HttpResponse(JsonResponse(serializer.data, safe=False))
