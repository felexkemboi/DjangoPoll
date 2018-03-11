from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
 
from .models import Question,Choice



class  IndexView(generic.ListView):
	template_name = '/polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		#return the last five published questions
	 return Question.objects.order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    models = Question
    template_name = '/polls/detail.html'

class ResultsView(generic.DetailView):
    models = Question
    template_name = '/polls/detail.html'


def vote(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	try: 
		# request.POST['choice'] returns the ID of the selected choice
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#display the question voting form
		return render(request, 'polls/detail.html' ,{ 
        'question' : question,
        'error_message':"You didn't select a choice"
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#Always return an HttpResponseRedirect after successfully dealing 
		#with POST data,this prevents  data from being posted twice 
		# if a user clicks the back button
		return HttpResponseRedirect(reverse('polls:results',args = (question.id,)))
   