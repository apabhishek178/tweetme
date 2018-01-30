from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Tweet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import TweetModelForm
from.mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet
#Create
class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweet/create_view.html'
    #success_url = reverse_lazy("tweet:detail") instead of this get_absolute_url is created in models.py
    login_url = "/admin/"
    #checking validation of the form before posting the data
    '''def form_valid(self, form):
        #to check user authentication
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(TweetCreateView,self).form_valid(form)
        else:
            #to tell that user must be logged in
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
            return self.form_invalid(form)'''

#function based view of TweetCreateView
'''def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("/tweet/create")

    else:
        context = {
            "form": form
        }
        return render(request, "tweet/create_view.html", context)'''

#Retrieve
class TweetDetailView(DetailView):
    #template_name = "tweet/detail_view.html"
    queryset = Tweet.objects.all()

    '''def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Tweet,pk=pk)
        return obj

    #type of context data, in this case it is object
    def get_context_data(self,*args, **kwargs):
        context = super(TweetDetailView,self).get_context_data(*args, **kwargs)
        print(context)
        return context'''

class TweetListView(ListView):
    #template_name = "tweet/list_view.html"
    def get_queryset(self):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            #searching for the searched content in the tweet and return the tweet if found
            #checkout making queries in database from django documentation
            qs = qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query)
            )
        return  qs
    #type of context data, in this case it is object_list
    def get_context_data(self,*args, **kwargs):
        context = super(TweetListView,self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")

        return context





'''def tweet_detail_view(request,id=1):
    obj = Tweet.objects.get(id=id) #get from the database
   #obj = get_object_or_404(Tweet, pk=pk) #getting data or raising a 404 error 
    context = {
        "object": obj
    }
    return render(request, "tweet/detail_view.html", context)

def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "tweet/list_view.html", context)'''


#Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweet/update_view.html'
    success_url = reverse_lazy("tweet:list")

#Delete
class TweetDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Tweet.objects.all()
    template_name = "tweet/delete_confirm.html"
    success_url = reverse_lazy("tweet:list")
