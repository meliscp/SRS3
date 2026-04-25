from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Category
from .forms import ProjectForm

def index(request):
    return render(request, 'projects/index.html')

def project_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    
    if category_id:
        projects = Project.objects.filter(category_id=category_id)
    else:
        projects = Project.objects.all()
        
    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'categories': categories
    })

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})