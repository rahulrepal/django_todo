from django import forms
from .models import Todo
class AddTodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ["title","desc"]

        widgets = {
            "title":forms.TextInput(attrs={"id":"title","class":"form-control"}),
            "desc":forms.Textarea(attrs={"id":"desc","class":"form-control"})
        }

        labels = {
            "desc":"Description"
        }

