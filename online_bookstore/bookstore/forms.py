from django import forms
from .models import Book


class book_form(forms.ModelForm):
    choice=[
        ("Fiction","Fiction"),
        ("Non-Fiction","Non-Fiction"),
        ("Horror","Horror"),
        ("Romance","Romance"),
        ("Sci-fi ","Sci-fi "),
        ("Mystery","Mystery"),
        ("Thriller","Thriller"),
        ("Comedy","Comedy"),
        ("Other","Other"),
    ]
    genre=forms.ChoiceField(choices=choice,initial="other")

    genre.widget.attrs.update({"class":"form-select"})
    class Meta:
        model=Book
        fields=["title","description","url","genre","author","rating","price","publication_date"]
         

        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control title","placeholder":"Enter the title","autocomplete":"off"}),
            "description":forms.Textarea(attrs={"class":"form-control content","placeholder":"Book Description","autocomplete":"off","maxlength":1000,"rows":7}),
            "url":forms.URLInput(attrs={"class":"form-control title","placeholder":"Image URL","autocomplete":"off"}),
            "price":forms.NumberInput(attrs={"class":"form-control title","placeholder":"Enter the Price","autocomplete":"off" ,  "type":"number"}),
            "author":forms.TextInput(attrs={"class":"form-control title","placeholder":"Enter the Author name","autocomplete":"off"}),
            "rating":forms.NumberInput(attrs={"class":"form-control title","placeholder":"Enter the Ratings","autocomplete":"off" , "type":"number"}),
            "publication_date":forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form-control title datepicker","placeholder":"Enter the Publication Date","autocomplete":"off" , "type":"date"}),
        }

        labels={
            "title": "Name of the Book",
            "url":"Image URL",
            "publication_date": "Date of Publication",
            "author" : "Author Name",
            "description" : "Book Description",
            "rating": "User Ratings",

        }
        
       