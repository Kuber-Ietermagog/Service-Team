from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView
from django.template.loader import render_to_string, get_template

# Create your views here.

class ClockView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'clock_card/clock.html')

# class ClockEventCreateView(CreateView):
#     fields = "__all__"
#     model = ClockEntry
#
#     def get_initial(self):
#         initial = super(ClockEventCreateView, self).get_initial()
#         initial.update({})
