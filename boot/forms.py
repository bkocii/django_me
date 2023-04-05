from django.forms import ModelForm
from .models import Students
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class RegisterStudent(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'last_name', 'course_name', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2 my-2 py-2'
        self.helper.field_class = 'col-md-6 my-2 py-2'
        self.fields['course_name'].widget.attrs['class'] = 'form-select'
        self.helper.layout = Layout(
            Fieldset(
                'PLEASE PROVIDE FOLLOWING INFO:',
                'name',
                'last_name',
                'course_name',
                'email',
                'phone',
            ),
            Submit('submit', 'Submit', css_class='btn-secondary'),
        )
