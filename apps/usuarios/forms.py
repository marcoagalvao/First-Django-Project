from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(label="Nome de Login", 
                                 required= True, 
                                 max_length= 100, 
                                 widget=forms.TextInput(
                                     attrs={
                                         "class": "form-control",
                                         "placeholder": "Digite seu nome de Login", 
                                         }
                                     )
                                 )
    senha = forms.CharField(label="Senha", 
                            required= True, 
                            max_length=70, 
                            widget=forms.PasswordInput(
                                attrs={
                                    "class": "form-control",
                                    "placeholder": "Digite sua senha",
                                    }
                                )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label="Nome completo", 
                                 required= True, 
                                 max_length= 100, 
                                 widget=forms.TextInput(
                                     attrs={
                                         "class": "form-control",
                                         "placeholder": "Digite seu nome completo", 
                                         }
                                     )
    )
    email = forms.EmailField(label="Email",
                            required= True, 
                            max_length= 100,
                            widget=forms.EmailInput(
                                     attrs={
                                         "class": "form-control",
                                         "placeholder": "Digite seu email", 
                                         }
                                     )
    )
    senha_1 = forms.CharField(label="Senha", 
                            required= True, 
                            max_length=70, 
                            widget=forms.PasswordInput(
                                attrs={
                                    "class": "form-control",
                                    "placeholder": "Digite sua senha",
                                    }
                                )
    )
    senha_2 = forms.CharField(label="Confirmação da senha", 
                            required= True, 
                            max_length=70, 
                            widget=forms.PasswordInput(
                                attrs={
                                    "class": "form-control",
                                    "placeholder": "Digite sua senha novamente",
                                    }
                                )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        
        if nome:
            nome = nome.strip() #tira o espaço do inicio e do fim da string
            if " " in nome:
                raise forms.ValidationError("O nome de cadastro não pode conter espaços")
            else: 
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")
        
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas digitadas não são iguais")
            else:
                return senha_2