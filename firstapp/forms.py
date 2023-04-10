from django import  forms

class UserForm(forms.Form):
    name=forms.CharField(label='Имя',required=False,help_text="не болие 15 символов",initial="ведите ФИО")
    age=forms.IntegerField(label='Возраст',required=False,initial='0',help_text='только цифры')
    coment=forms.ChoiceField(label='коминтариий',widget=forms.Textarea, initial='оставте коментари')
    basket=forms.BooleanField(label='положить товар в корзину',required=False)
    vyb=forms.NullBooleanField(label='Выберите')
    email=forms.EmailField(label='Адрес электроной почты',help_text=' должин быть символ @',required=False)
    slag_text=forms.SlugField(label='введите текст',required=False)
    h=forms.ComboField(fields=[forms.SlugField(),forms.EmailField()],required=False)
    #fp=forms.FilePathField(label='выберите фаил',path=r'C:\~\Web_1\hello\firstapp',allow_files=True,allow_folders=True)
    f=forms.FileField(label='фаил',required=False)
    IF=forms.ImageField(label='Изоброжение',required=False)
    l=forms.ChoiceField(label='язык',choices=((1,'Англиский'),(2,'Немецкий'),(3,'Французкий')),required=False)
    field_order = ['coment','age','name']