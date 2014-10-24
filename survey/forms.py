# encoding: utf-8
import uuid
from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.forms import models
from survey.models import Question, Category, Survey, Response, AnswerText, AnswerRadio, AnswerSelect, AnswerInteger, AnswerSelectMultiple
from convocat.forms import MunicipioChoice, MyDateWidget
from django_select2 import Select2Widget

# blatantly stolen from 
# http://stackoverflow.com/questions/5935546/align-radio-buttons-horizontally-in-django-forms?rq=1
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class ResponseForm(models.ModelForm):
	#municipio_nacimiento = MunicipioChoice()
	class Meta:
		model = Response
		fields = tuple()	
		#fields = ('nombre','jornada', 'institucion') #('interviewer', 'interviewee', 'conditions', 'comments')
		#widgets = {
		#	'institucion' : Select2Widget(),
		#	#'fecha_nacimiento' : MyDateWidget(),
		#}

	def __init__(self, *args, **kwargs):
		# expects a survey object to be passed in initially
		survey = kwargs.pop('survey')
		self.survey = survey
		super(ResponseForm, self).__init__(*args, **kwargs)
		self.uuid = random_uuid = uuid.uuid4().hex	

		# add a field for each survey question, corresponding to the question
		# type as appropriate.
		data = kwargs.get('data')
		for q in survey.questions():
			if q.question_type == Question.TEXT:
				self.fields["question_%s" % q.number] = forms.CharField(label=q.text, 
					widget=forms.TextInput, required=q.required)
			elif q.question_type == Question.RADIO:
				question_choices = q.get_choices()
				self.fields["question_%s" % q.number] = forms.ChoiceField(label=q.text, 
					widget=forms.RadioSelect(), #renderer=HorizontalRadioRenderer), 
					choices = question_choices, required=q.required)
			elif q.question_type == Question.SELECT:
				question_choices = q.get_choices()
				# add an empty option at the top so that the user has to
				# explicitly select one of the options
				question_choices = tuple([('', '-------------')]) + question_choices
				self.fields["question_%s" % q.number] = forms.ChoiceField(label=q.text, 
					widget=forms.Select, choices = question_choices, required=q.required)
			elif q.question_type == Question.SELECT_MULTIPLE:
				question_choices = q.get_choices()
				self.fields["question_%s" % q.number] = forms.MultipleChoiceField(label=q.text, 
					widget=forms.CheckboxSelectMultiple, choices = question_choices, required=q.required)
			elif q.question_type == Question.INTEGER:
				self.fields["question_%s" % q.number] = forms.IntegerField(label=q.text, required=q.required)				
			
			# if the field is required, give it a corresponding css class.
			if q.required:
				self.fields["question_%s" % q.number].required = True
				self.fields["question_%s" % q.number].widget.attrs["class"] = "required"
			else:
				self.fields["question_%s" % q.number].required = False
			
				
			# add the category as a css class, and add it as a data attribute
			# as well (this is used in the template to allow sorting the
			# questions by category)
			if q.category:
				classes = self.fields["question_%s" % q.number].widget.attrs.get("class")
				if classes:
					self.fields["question_%s" % q.number].widget.attrs["class"] = classes + (" cat_%s" % q.category.name)
				else:
					self.fields["question_%s" % q.number].widget.attrs["class"] = (" cat_%s" % q.category.name)
				self.fields["question_%s" % q.number].widget.attrs["category"] = q.category.name


			# initialize the form field with values from a POST request, if any.
			if data:
				self.fields["question_%s" % q.number].initial = data.get('question_%s' % q.number)

	'''
	def clean_numero_documento(self):
		# Revisar que esta misma persona (por numero_documento), no haya llenado esta misma encuesta
		doc = self.cleaned_data['numero_documento']
		if Response.objects.filter(survey_id=self.survey, numero_documento=doc).exists():
			raise ValidationError('Ya se ha diligenciado la encuesta usando este número de documento')
		else:
			return doc
	'''

	def save(self, commit=True):
		# save the response object
		response = super(ResponseForm, self).save(commit=False)
		response.survey = self.survey
		response.interview_uuid = self.uuid
		response.save()

		# create an answer object for each question and associate it with this
		# response.

		questions = { q.number: q for q in self.survey.question_set.all() }

		for field_name, field_value in self.cleaned_data.iteritems():
			if field_name.startswith("question_"):
				# warning: this way of extracting the id is very fragile and
				# entirely dependent on the way the question_id is encoded in the
				# field name in the __init__ method of this form class.
				q_number = field_name.split("_")[1]
				#q = Question.objects.get(survey=self.survey ,number=q_number)
				q = questions[q_number]

				if q.question_type == Question.TEXT:
					a = AnswerText(question = q)
					a.body = field_value
				elif q.question_type == Question.RADIO:
					a = AnswerRadio(question = q)	
					a.body = field_value
				elif q.question_type == Question.SELECT:
					a = AnswerSelect(question = q)	
					a.body = field_value
				elif q.question_type == Question.SELECT_MULTIPLE:
					a = AnswerSelectMultiple(question = q)	
					a.body = field_value
				elif q.question_type == Question.INTEGER:	
					a = AnswerInteger(question = q)	
					a.body = field_value
				a.response = response
				a.save()
		return response

class CodigoEncuestaForm(forms.Form):
    registro = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Escriba el código de acceso a las encuestas'}))