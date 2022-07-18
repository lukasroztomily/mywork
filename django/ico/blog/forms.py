from django import forms
from .models import Blog


class AddBlogForm(forms.ModelForm):
    
    
    class Meta:
        model = Blog
        fields = ['title_sk', 'text_sk', 'headline_sk', 'title_en', 'text_en', 'headline_en', 'title_de', 'text_de', 'headline_de', 'is_published']
        widgets = {
            'headline_sk': forms.Textarea(attrs={"rows":3, 'maxlength':250}),
            'headline_en': forms.Textarea(attrs={"rows":3, 'maxlength':250}),
            'headline_de': forms.Textarea(attrs={"rows":3, 'maxlength':250})
           }



    def __init__(self, *args, **kwargs):
        super(AddBlogForm, self).__init__(*args, **kwargs)
        self.fields['title_sk'].widget.attrs['placeholder'] = 'Enter title'
        self.fields['text_sk'].widget.attrs['placeholder'] = 'Enter description'
        self.fields['headline_sk'].widget.attrs['placeholder'] = 'Enter headline'
        self.fields['title_en'].widget.attrs['placeholder'] = 'Enter title'
        self.fields['text_en'].widget.attrs['placeholder'] = 'Enter description'
        self.fields['headline_en'].widget.attrs['placeholder'] = 'Enter headline'
        self.fields['title_de'].widget.attrs['placeholder'] = 'Enter title'
        self.fields['text_de'].widget.attrs['placeholder'] = 'Enter description'
        self.fields['headline_de'].widget.attrs['placeholder'] = 'Enter headline'
        self.fields['is_published'].widget.attrs['placeholder'] = 'Enter is_published'
        for field in self.fields:
                self.fields[field].widget.attrs['class'] =    'form-control'

        self.fields['is_published'].widget.attrs['class'] = "form-input"





class EditBlogForm(forms.ModelForm):
    
    
    class Meta:
        model = Blog
        fields = fields = ['title_sk', 'text_sk', 'headline_sk', 'title_en', 'text_en', 'headline_en', 'title_de', 'text_de', 'headline_de']
        widgets = {
            'headline_sk': forms.Textarea(attrs={"rows":3, 'maxlength':250}),
            'headline_en': forms.Textarea(attrs={"rows":3, 'maxlength':250}),
            'headline_de': forms.Textarea(attrs={"rows":3, 'maxlength':250})
           }

    def __init__(self, *args, **kwargs):
        super(EditBlogForm, self).__init__(*args, **kwargs)
        self.fields['title_sk'].widget.attrs['placeholder'] = 'Enter title'
        self.fields['text_sk'].widget.attrs['placeholder'] = 'Enter description'
        self.fields['headline_sk'].widget.attrs['placeholder'] = 'Enter headline'
        self.fields['title_en'].widget.attrs['placeholder'] = 'Enter title'
        self.fields['text_en'].widget.attrs['placeholder'] = 'Enter description'
        self.fields['headline_en'].widget.attrs['placeholder'] = 'Enter headline'
        self.fields['title_de'].widget.attrs['placeholder'] = 'Enter title'
        self.fields['text_de'].widget.attrs['placeholder'] = 'Enter description'
        self.fields['headline_de'].widget.attrs['placeholder'] = 'Enter headline'
        
        for field in self.fields:
                self.fields[field].widget.attrs['class'] =    'form-control'

