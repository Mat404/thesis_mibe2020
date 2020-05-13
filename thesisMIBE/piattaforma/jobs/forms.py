from django import forms
from .models import post_job

class post_jobModelForm(forms.ModelForm):
    class Meta:
        model = post_job
        fields = ["posizione", "nome_azienda", "descrizione","requisiti", "email_referente","categoria"]
        widgets = {
            "posizione": forms.TextInput(attrs={"placeholder": "Inserisci Qui"})
        }
