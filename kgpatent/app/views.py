
from django.db.models import Q


from django.views.generic import ListView, DetailView
from .models import Mark, Applicant, Patent, Code

class Home(ListView):
    model = Mark
    context_object_name = 'marks'
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(registration_id__icontains=query) |
                Q(date_of_submission__icontains=query) |
                Q(code__code__icontains=query) |
                Q(code__description__icontains=query) |
                Q(applicant__title__icontains=query) |
                Q(applicant__adress__icontains=query) |
                Q(applicant__country__icontains=query) |
                Q(patent__title__icontains=query) |
                Q(patent__adress__icontains=query) |
                Q(patent__tel__icontains=query) |
                Q(patent__email__icontains=query)
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Applicant.objects.all()
        context['programs'] = Patent.objects.all()
        context['aboutkeus'] = Code.objects.all()
        return context

#
# class MarkDetailView(DetailView):
#     model = Mark
#     template_name = 'mark_detail.html'
#     context_object_name = 'mark'
# def detail(request, table1_id):
#     # Получение записи по идентификатору
#     table1_item = get_object_or_404(Table1, pk=table1_id)
#
#     context = {
#         'table1_item': table1_item,
#     }
#     return render(request, 'detail.html', context)
