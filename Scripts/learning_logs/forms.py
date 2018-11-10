from django import forms
from .models import Topic
from .models import Entry

class TopicForm(forms.ModelForm):
    """创建科目表单类"""
    class Meta:
        model=Topic
        fields=['text']
        labels={'text':''}
class EntryForm(forms.ModelForm):
    """创建条目表单类"""
    class Meta:
        model=Entry
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}