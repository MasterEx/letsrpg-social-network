from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import int_to_base36
from django.template import Context, loader
from django import forms
from django.core.mail import send_mail

class UserCreationForm(forms.ModelForm):
	username = forms.RegexField(label="Username", max_length=30, regex=r'^[\w.@+-]+$',
								help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
								error_messages = {'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput,
								help_text = "Enter the same password as above, for verification.")
	email1 = forms.EmailField(label="Email", max_length=75)
	email2 = forms.EmailField(label="Email confirmation", max_length=75,
							  help_text = "Enter your email address again. A confirmation email will be sent to this address.")

	class Meta:
		model = User
		fields = ("username",)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1", "")
		password2 = self.cleaned_data["password2"]
		if password1 != password2:
			raise forms.ValidationError("The two password fields didn't match.")
		return password2
	
	def clean_email1(self):
		email1 = self.cleaned_data["email1"]
		users_found = User.objects.filter(email__iexact=email1)
		if len(users_found) >= 1:
			raise forms.ValidationError("A user with that email already exist.")
		return email1

	def clean_email2(self):
		email1 = self.cleaned_data.get("email1", "")
		email2 = self.cleaned_data["email2"]
		if email1 != email2:
			raise forms.ValidationError("The two email fields didn't match.")
		return email2

	def save(self, commit=True, domain_override=None,
			 email_template_name='registration/signup_email.html',
			 use_https=False, token_generator=default_token_generator):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.email = self.cleaned_data["email1"]
		user.is_active = False
		if commit:
			user.save()
		if not domain_override:
			current_site = Site.objects.get_current()
			site_name = current_site.name
			domain = current_site.domain
		else:
			site_name = domain = domain_override
		t = loader.get_template(email_template_name)
		c = {
			'email': user.email,
			'domain': domain,
			'site_name': site_name,
			'uid': int_to_base36(user.id),
			'user': user,
			'token': token_generator.make_token(user),
			'protocol': use_https and 'https' or 'http', 
			}
		send_mail("Confirmation link sent on %s" % site_name,
				  t.render(Context(c)), 'letsrpg.info@gmail.com', [user.email])
		return user

class UserProfileForm(forms.Form):
	last_name = forms.CharField(max_length=20,label='Last name')
	first_name = forms.CharField(max_length=20,label='First name')
	age = forms.IntegerField()
	location = forms.CharField(max_length=30,label='Location')
	#avatar = models.FileField(upload_to='avatars')
	notes = forms.CharField(widget=forms.Textarea)
	#favorite_fantasy_game = models.CharField(max_length=20)
	#favorite_race = models.CharField(max_length=20)
	#favorite_class = models.CharField(max_length=20)
