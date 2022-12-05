from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
from posts.models import Post
from django.db.models import Q, Count, Case, When
from comments.forms import FormComment
from comments.models import Comment
from django.contrib import messages


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('category_post')
        qs = qs.order_by('-id').filter(publish_post=True)
        qs = qs.annotate(
            comments_number=Count(
                Case(
                    When(comment__publish_comment=True, then=1)
                )
            )
        )

        return qs


class PostSearch(PostIndex):
    template_name = 'posts/search_post.html'

    def get_queryset(self):
        qs = super().get_queryset()
        term = self.request.GET.get('term')

        if not term:
            return qs

        qs = qs.filter(
            Q(title_post__icontains=term) |
            Q(author_post__first_name__iexact=term) |
            Q(content_post__icontains=term) |
            Q(summary_post__icontains=term) |
            Q(category_post__name_cat__iexact=term)
        )

        return qs


class PostCategory(PostIndex):
    template_name = 'posts/category_post.html'

    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)

        if not category:
            return qs

        qs = qs.filter(category_post__name_cat__iexact=category)

        return qs


class PostDetails(View):
    template_name = 'posts/details_post.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, publish_post=True)
        self.context = {
            'post': post,
            'comments': Comment.objects.filter(post_comment=post, publish_comment=True),
            'form': FormComment(request.POST or None),
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.context['form']

        if not form.is_valid():
            return render(request, self.template_name, self.context)

        comment = form.save(commit=False)

        if request.user.is_authenticated:
            comment.user_comment = request.user

        comment.post_comment = self.context['post']
        comment.save()
        messages.success(request, 'Your comment has been sent for review')
        return redirect('post_details', pk=self.kwargs.get('pk'))
