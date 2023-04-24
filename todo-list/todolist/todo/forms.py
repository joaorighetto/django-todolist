from django import forms

from .models import Todo


PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]


class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    class Meta:
        model = Todo
        fields = ['task', 'priority', 'user']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(choices=PRIORITY_CHOICES),
            'user': forms.HiddenInput(),
        }
