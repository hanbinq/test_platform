from django import forms
from .models import Project, Module

"""
class ProjectForm(forms.Form):
    name = forms.CharField(label="名称", max_length=100)
    describe = forms.CharField(label="描述", widget=forms.Textarea)
    status = forms.BooleanField(label="状态", required=False)
    # status = forms.ChoiceField(label="状态")
"""
class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ['create_time']


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        exclude = ['create_time']

