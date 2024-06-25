from django import forms
from django.contrib.auth.models import User
from .models import Record, Comment, Folder

class AddRecordForms(forms.ModelForm):
    BFE_Nummer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"BFE Nummer", "class":"form-control"}))
    Adresse = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Adresse", "class":"form-control"}))
    By = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"By", "class":"form-control"}))
    Kommune = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Kommune", "class":"form-control"}))
    Postnummer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Postnummer", "class":"form-control"}))
    Region = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Region", "class":"form-control"}))
    Kontaktperson = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Kontaktperson", "class":"form-control"}))
    Mail = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Mail", "class":"form-control"}))
    Telefonnummer = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Telefonnummer", "class":"form-control"}))
    m2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"m2", "class":"form-control"}))
    Kommuneplan = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Kommuneplan", "class":"form-control"}))
    Lokalplan = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Lokalplan", "class":"form-control"}))
    Formaal = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Formål", "class":"form-control"}))
    Pris_Hektar = forms.DecimalField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Pris pr. Hektar", "class":"form-control"}))
    Forfaldsdato =  forms.DateField(required=False, input_formats=['%Y-%m-%d'], widget=forms.widgets.TextInput(attrs={"placeholder":"Forfaldsdato", 'autocomplete':'off', "class":"form-control"}))
    Opfølgningsdato = forms.DateField(required=False, input_formats=['%Y-%m-%d'], widget=forms.widgets.TextInput(attrs={"placeholder":"Opfølgningsdato", 'autocomplete':'off', "class":"form-control"}))


    class Meta:
        model = Record
        exclude = ("user",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        if self.user:
            comment.user = self.user
        if commit:
            comment.save()
        return comment

class ImportRecordDataForm(forms.Form):
    record_data = forms.FileField(required=True)



class CheckboxForm(forms.Form):
    class Meta:
        model = Record
        fields = ['Ja', 'Nej', 'Sendt til DLA']



class NewFolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['record', 'name']

    def __init__(self, *args, **kwargs):
        super(NewFolderForm, self).__init__(*args, **kwargs)
        self.fields['record'].queryset = Record.objects.all()

