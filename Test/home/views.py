from django.shortcuts import render, redirect
from django.views.generic import TemplateView


from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.forms import HomeForm
from home.models import Actividad
# Create your views here.



class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get (self, request):
        form = HomeForm()
        posts = Actividad.objects.all()
        users = User.objects.all()
        #print (posts)

        args = {'form': form, 'posts': posts, 'users': users}
        return render(request, self.template_name, args)

class EstudianteView(TemplateView):
    template_name = 'home/estudiante.html'

    def get (self, request):
        users = User.objects.all()
        #print (posts)

        args = { 'users': users}
        return render(request, self.template_name, args)

#@login_required
class PublishView(TemplateView):
    template_name = 'home/publish.html'

    def get (self, request):
        form = HomeForm()
        args = {'form': form}
        return render (request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            #text = form.cleaned_data['nombre']
            form = HomeForm()
            return redirect('/home/')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

#def publish(request):
#    user = request.user
#    if user.userprofile.supervisor == True:
