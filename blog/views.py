from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, ContactForm


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/index.html', context)

class BlogListView(ListView):
	model = Post
	template_name = 'blog/index.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 3

class BlogDetailView(DetailView):
	model = Post

class BlogCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'		

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title':'About Us'})


def contact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		subject = request.POST.get('subject')
		email = request.POST.get('email')
		message = request.POST.get('message')
		ContactForm.objects.create(
			name = name,
			subject = subject,
			email = email,
			message = message
		)
		return render(
			request,
			'blog/contact.html',
			{
				'msg':'Details have been saved. We will get back to you.'
			}
		)
	else:
		return render(request, 'blog/contact.html')	



