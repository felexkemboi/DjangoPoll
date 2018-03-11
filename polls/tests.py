import datetime
from django.test import TestCase

from django.utils import timezone

from .models import Question 


class QuestionModelTests(TestCase):

      def test_was_published_recently_with_future_question(self):
         """was_published_recently() returns False for Questions whose pub_date is in future"""
         time = timezone.now() + datetime.timedelta(days=30)
         future_question = Question(pub_date = time)
         self.assertIs(future_question.was_published_recently(),False) 

     def  test_was_published_recently_with_old_question(self):
     	 """"was published recently returns False for Qquestions whose pub_date is older than 1 day"""
     	 time = timezone.now() - datetime.timedelta(days=1,seconds = 1)
     	 old_question = Question(pub_date = time)
     	 self.assertIs(old_question.was_published_recently(),False)

     def test_was_published_recently_with_recent_question(self):
     	 """"was published_recently() returns True for Questions whose pub_date is within the last day"""
     	 time = timezone.now() - datetime.timedelta(hrs=23 ,mins=59,seconds= 59)
     	 recent_question = Question(pub_date= time)
     	 self.assertIs(recent_question.was_published_recently(),True)
