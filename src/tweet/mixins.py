from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):
    def form_valid(self, form):
        #to check user authentication
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin,self).form_valid(form)
        else:
            #to tell that user must be logged in
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
            return self.form_invalid(form)

class UserOwnerMixin(FormUserNeededMixin, object):
    def form_valid(self, form):
        #to check user authentication
        if form.instance.user == self.request.user:
            return super(FormUserNeededMixin,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This user is not allowed to make updation"])
            return self.form_invalid(form)

