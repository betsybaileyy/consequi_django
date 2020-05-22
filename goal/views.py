from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from goal.models import Achievement, Goal

class IndexView(generic.ListView):
    template_name = 'templates/homeScreen.html'
    # context_object_name = 'latest_question_list'


    def index(request):
        all_achievements = Achievement.objects.filter(name="Hello World")
        all_goals = Goal.objects.all()
        completed_goals = Goal.done(True)
        open_goals = Goal.done(False)
        # return render(request, 'templates/homeScreen.html')
        return HttpResponse(f"# of Achievements: <br># of Goals: {all_achievements}<br> # of goals: {len(all_goals)} # of completed goals: {len(completed_goals)}. # of open goals{len(open_goals)}")




# def vote(request, goal_id):
#     goal = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))