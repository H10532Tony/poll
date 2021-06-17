from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView,CreateView,UpdateView,DeleteView
from .models import Poll, Option
from .models import *
from django.urls import reverse

# Create your views here.
def poll_list(req):
    data = Poll.objects.all()
    return render(req, 'poll_list.html', {'polls':data})

class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['option_list'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        return ctx

class PollVote(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        op = Option.objects.get(id=self.kwargs['oid'])
        op.count += 1
        op.save()
        return "/poll/{}/".format(op.poll_id)

    class PollCreate(CreateView):
        model = Poll
        fields = ['subject','desc']    # 指定要顯示的欄位
        #success_url = '/poll/'  # 成功新增後要導向的路徑
        def get_success_url(self):

            return "/poll/{}/".format(self.object.id)
        template_name = 'general_form.html' # 要使用的頁面範本
class PollDelete(DeleteView):
    model = Poll
    success_url = '/poll/'
    template_name = "confirm_delete.html"
class OptionUpdate(UpdateView):
    model = Option
    fields = ['title']
    template_name = 'general_form.html'
    # 修改成功後返回其所屬投票主題檢視頁面
    def get_success_url(self):
        return '/poll/'+str(self.object.poll_id)+'/'
class OptionDelete(DeleteView):
    model = Option
    template_name = 'confirm_delete.html'
    # 刪除成功後返回其所屬投票主題檢視頁面
    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll_id})