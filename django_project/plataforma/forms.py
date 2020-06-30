from django import forms

# Formulario Solução Gráfica:

class AlgoritmoGrafico(forms.Form):
	'''tipos = (
		("Maximizar"),
		("Minimizar"),
	)'''
	funcao_objetivo_tipo = forms.ChoiceField(choices=[(0,"Minimizar"),(1,"Maximizar")], widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
	funcao_objetivo_x1 = forms.DecimalField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
	funcao_objetivo_x2 = forms.DecimalField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
	restricao1_x1 = forms.DecimalField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
	restricao1_x2 = forms.DecimalField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'name': 'test'}))

'''
class UsuariosCadastrarForm(forms.Form):
    username = forms.CharField(label='Username', max_length=10)
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nome', max_length=50)
    last_name = forms.CharField(label='Sobrenome', max_length=50)
    email = forms.EmailField(label='E-mail', required=False)
    admin = forms.BooleanField(label='User administrador', required=False)

def modificar_form(user=None,request=None):
	class UsuariosModificarForm(forms.Form):
	    username = forms.CharField(label='Username', max_length=10, widget=forms.TextInput(attrs={'value': user.username}))
	    #password = forms.CharField(label='Password', disabled=True)
	    first_name = forms.CharField(label='Nome', max_length=50, widget=forms.TextInput(attrs={'value': user.first_name}))
	    last_name = forms.CharField(label='Sobrenome', max_length=50, widget=forms.TextInput(attrs={'value': user.last_name}))
	    email = forms.EmailField(label='E-mail', required=False, widget=forms.TextInput(attrs={'value': user.email}))
	    admin = forms.BooleanField(label='User administrador', required=False, initial= user.is_staff)
	if request: 
		print('oi')
		return UsuariosModificarForm(request)
	else: 
		return UsuariosModificarForm()

# Login

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput)
	'''