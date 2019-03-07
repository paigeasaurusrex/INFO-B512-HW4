from django.shortcuts import render
from personalweb.models import Projects, Skills
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	projects=Projects.objects.all()
	skills=Skills.objects.all()
	return render(request, 'personalweb/index.html', {'projects': projects, 'skills': skills})
	
def delete_project(request, project_id):
	project_id=int(project_id)
	Projects.objects.filter(Project_ID=project_id).delete()
	projects=Projects.objects.all()
	skills=Skills.objects.all()
	return render(request, 'personalweb/index.html', {'projects': projects, 'skills': skills})
	
def delete_skill(request, skill_id):
	skill_id=int(skill_id)
	Skills.objects.filter(Skill_ID=skill_id).delete()
	projects=Projects.objects.all()
	skills=Skills.objects.all()
	return render(request, 'personalweb/index.html', {'projects': projects, 'skills': skills})
	
def insert_project(request):
	project_id=request.POST.get('project_id')
	project_descrip=request.POST.get('project_descrip')
	project_year=request.POST.get('project_year')
	new=Projects(Project_ID=project_id, Project_Descrip=project_descrip, Project_year=project_year)
	new.save()
	projects=Projects.objects.all()
	skills=Skills.objects.all()
	return render(request, 'personalweb/index.html', {'projects': projects, 'skills': skills})