from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from .forms import QuestionForm, ChoiceForm
from django.forms import modelformset_factory
from django.forms import formset_factory
from .models import Question, Choice

# Get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    print(f"Questions retrieved: {latest_question_list}")  # Debug print
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})

# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choices = request.POST.getlist('choice')
        if not selected_choices:
            raise KeyError
    except KeyError:
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        for choice_id in selected_choices:
            selected_choice = question.choice_set.get(pk=choice_id)
            selected_choice.votes += 1
            selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def create_question(request):
    ChoiceFormSet = modelformset_factory(Choice, form=ChoiceForm, extra=1, can_delete=True)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        formset = ChoiceFormSet(request.POST, queryset=Choice.objects.none())

        print(f"Question form valid: {question_form.is_valid()}")
        if not question_form.is_valid():
            print(f"Question form errors: {question_form.errors}")

        print(f"Formset valid: {formset.is_valid()}")
        if not formset.is_valid():
            print(f"Formset errors: {formset.errors}")

        if question_form.is_valid() and formset.is_valid():
            question = question_form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    choice = form.save(commit=False)
                    choice.question = question
                    choice.save()
            print(f"Question created: {question}")
            return redirect('polls:index')
        else:
            print("Form submission failed")
    else:
        question_form = QuestionForm()
        formset = ChoiceFormSet(queryset=Choice.objects.none())

    return render(request, 'polls/create_question.html', {
        'question_form': question_form,
        'formset': formset,
    })

def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        question.delete()
        return redirect('polls:index')
    return render(request, 'polls/delete_question_confirm.html', {'question': question})


from django.shortcuts import get_object_or_404, render, redirect
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm
from django.forms import modelformset_factory

def update_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ChoiceFormSet = modelformset_factory(Choice, form=ChoiceForm, extra=1, can_delete=True)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST, instance=question)
        formset = ChoiceFormSet(request.POST, queryset=question.choice_set.all())

        if question_form.is_valid() and formset.is_valid():
            question = question_form.save()
            for form in formset:
                if form.cleaned_data:
                    if form.cleaned_data.get('DELETE'):
                        if form.instance.pk:
                            form.instance.delete()
                    else:
                        choice = form.save(commit=False)
                        choice.question = question
                        choice.save()
            return redirect('polls:detail', question_id=question.id)
    else:
        question_form = QuestionForm(instance=question)
        formset = ChoiceFormSet(queryset=question.choice_set.all())

    return render(request, 'polls/update_question.html', {
        'question_form': question_form,
        'formset': formset,
        'question': question,
    })