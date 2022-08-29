from django import forms
from .models import Post, Category, Contact

# choices = [('English Premire League', 'English Premire League'),
#             ('Laliga', 'Laliga'),
#              ('UEFA Champians League', 'UEFA Champians League'),
#             ('Tactical Theory', 'Tactical Theory'),
#             ('Others', 'Others'),]
choices =  Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'author', 'Category', 'body' ,'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Your Blog Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'Category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),


        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'text')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Your Name'}),
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Input what you want to say'}),


        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Your Blog Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),



        }
