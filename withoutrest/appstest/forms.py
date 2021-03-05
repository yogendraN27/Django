from django import forms
from appstest.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal=self.cleaned_data['esal']
        print(inputsal)
        if inputsal<5000:
            print('Error is here')
            raise forms.ValidationError('the minimum salary shuold be 5000')
        return inputsal
    class Meta:
        model=Employee
        fields='__all__'