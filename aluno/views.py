from django.shortcuts import render,get_object_or_404,redirect
from .models import Aluno,Curso,Cidade
from .forms import AlunoForm, CidadeForm, CursoForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, ListView

# class AlunoCriar(CreateView):
#     model = Aluno
#     fields = '__all__'
#     template_name = 'aluno/form.html'
#     success_url = reverse_lazy('aluno_listar')

# class AlunoEditar(UpdateView):
#     model = Aluno
#     fields = '__all__'
#     template_name = 'aluno/form.html'
#     success_url = reverse_lazy('aluno_listar')
#     pk_url_kwarg = 'id'

# class AlunoListar(ListView):
#     model = Aluno
#     template_name = 'aluno/alunos.html'
#     context_object_name = 'alunos'

# class AlunoDeletar(DeleteView):
#     model = Aluno
#     success_url = reverse_lazy('aluno_listar')
#     pk_url_kwarg = 'id'

#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)

# class CursoCriar(CreateView):
#     model = Curso
#     fields = '__all__'
#     template_name = 'curso/form.html'
#     success_url = reverse_lazy('curso_listar')

# class CursoListar(ListView):
#     model = Curso
#     template_name = 'curso/cursos.html'
#     context_object_name = 'cursos'

# class CursoEditar(UpdateView):
#     model = Curso
#     fields = '__all__'
#     template_name = 'curso/form.html'
#     success_url = reverse_lazy('curso_listar')
#     pk_url_kwarg = 'id'

# class CursoDeletar(DeleteView):
#     model = Curso
#     fields = '__all__'
#     success_url = reverse_lazy('curso_listar')
#     pk_url_kwarg = 'id'

#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)


# class CidadeCriar(CreateView):
#     model = Cidade
#     fields = '__all__'
#     template_name = 'cidades/form.html'
#     success_url = reverse_lazy('cidade_listar')

# class CidadeListar(ListView):
#     model = Cidade
#     template_name = 'cidades/cidades.html'
#     context_object_name = 'cidades'

# class CidadeEditar(UpdateView):
#     model = Cidade
#     fields = '__all__'
#     template_name = 'cidades/form.html'
#     success_url = reverse_lazy('cidade_listar')
#     pk_url_kwarg = 'id'

# class CidadeDeletar(DeleteView):
#     model = Cidade
#     fields = '__all__'
#     success_url = reverse_lazy('cidade_listar')
#     pk_url_kwarg = 'id'

#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)

# class Index(TemplateView):
    
#     template_name = 'aluno/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['total_alunos'] = Aluno.objects.count()
#         context['total_cidades'] = Cidade.objects.count()
#         context['total_cursos'] = Curso.objects.count()
#         return context

def aluno_editar(request,id):
    aluno = get_object_or_404(Aluno,id=id)
   
    if request.method == 'POST':
        form = AlunoForm(request.POST,instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('aluno_listar')
    else:
        form = AlunoForm(instance=aluno)

    return render(request,'aluno/form.html',{'form':form})


def aluno_remover(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('aluno_listar') # procure um url com o nome 'lista_aluno'


def aluno_criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aluno_listar')
    else:
        form = AlunoForm()

    return render(request, "aluno/form.html", {'form': form})


def aluno_listar(request):
    alunos = Aluno.objects.all()
    context ={
        'alunos':alunos
    }
    return render(request, "aluno/alunos.html",context)


def cidade_criar(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cidade_listar')
    else:
        form = CidadeForm()

    return render(request, 'cidades/form.html', {'form' : form})


def cidade_listar(request):
    cidades = Cidade.objects.all()
    context = {
        'cidades' : cidades
    }
    return render(request, 'cidades/cidades.html', context)

def cidade_editar(request, id):
    cidade = get_object_or_404(Cidade, id=id)

    if request.method == 'POST':
        form = CidadeForm(request.POST, instance=cidade)

        if form.is_valid():
            form.save()
            return redirect('cidade_listar')
    else:
        form = CidadeForm(instance=cidade)

    return render(request,'cidades/form.html',{'form':form})

def cidade_deletar(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    cidade.delete()
    return redirect('cidade_listar') # procure um url com o nome 'lista_aluno'


def curso_criar(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_listar')
    else:
        form = CursoForm()

    return render(request, "curso/form.html", {'form': form})

def curso_listar(request):
    cursos = Curso.objects.all()
    context = {
        'cursos' : cursos
    }
    return render(request, 'curso/cursos.html', context)

def curso_editar(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)

        if form.is_valid():
            form.save()
            return redirect('curso_listar')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'curso/form.html', {'form' : form})


def curso_deletar(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('curso_listar')


def index(request):
    total_alunos = Aluno.objects.count()
    total_cidades = Cidade.objects.count()
    total_curso = Curso.objects.count()
    context = {
        'total_alunos' : total_alunos,
        'total_cidades' : total_cidades,
        'total_cursos' : total_curso
    }
    return render(request, "aluno/index.html",context)

