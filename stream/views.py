from django.shortcuts import render, redirect
from .models import Category, Video
from django.views import generic
from .forms import VideoForm
from django.urls import reverse_lazy


def index(request):
    categories = Category.objects.all()
    videos = Video.objects.all()
    video_list = Video.objects.order_by('-created')[:8]
    sort_list = Video.objects.order_by('-views')[:4]
    context = {
        'categories': categories,
        'videos': videos,
        'video_list': video_list,
        'sort_list': sort_list,
    }
    return render(request, 'stream-site/index.html', context)


class VideoDetailView(generic.DetailView):
    template_name = 'stream-site/video-page.html'
    model = Video

    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['videos'] = Video.objects.order_by('-views')[:6]
        return context

def view_order(request):
    return redirect('index')


def all_videos_date(request):
    video = Video.objects.order_by('-created')
    context = {
        'video': video,
    }
    return render(request, 'stream-site/all-videos.html', context)

def all_videos_popular(request):
    video = Video.objects.order_by('-views')
    context = {
        'video': video,
    }
    return render(request, 'stream-site/all-videos.html', context)

def admin2(request):
    categories = Category.objects.all()
    videos = Video.objects.all()
    context = {
        'categories': categories,
        'videos': videos,
    }
    return render(request, 'stream/index.html', context)

##################CATEGORIES######################
def categories(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'stream/categories.html', context)

class CategoryCreateView(generic.CreateView):
    template_name = 'stream/category_add.html'
    model = Category
    fields = ['name','description']
    success_url = reverse_lazy('admin2_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['categories'] = Category.objects.all()
        return context

class CategoryEditView(generic.UpdateView):
    template_name = 'stream/category_edit.html'
    model = Category
    fields = ['name', 'description']
    success_url = reverse_lazy('admin2_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['categories'] = Category.objects.all()
        return context


class CategoryDeleteView(generic.DeleteView):
    template_name = 'stream/category_delete.html'
    model = Category
    success_url = reverse_lazy('admin2_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

########################VIDEOS###########################

def admin2_videos(request):
    categories = Category.objects.all()
    videos = Video.objects.all()
    context = {
        'categories': categories,
        'videos': videos,
    }
    return render(request, 'stream/videos.html', context)

def category_video(request, pk):
    videos = Video.objects.filter(category=pk)
    categories = Category.objects.all()
    context = {
        'videos': videos,
        'categories': categories,
    }
    return render(request, 'stream/videos.html', context)


class VideoCreateView(generic.CreateView):
    template_name = 'stream/video_add.html'
    model = Video
    fields = ['category', 'title', 'description', 'url', 'duration', 'created']
    success_url = reverse_lazy('admin2_videos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['categories'] = Category.objects.all()
        return context

class VideoEditView(generic.UpdateView):
    template_name = 'stream/video_edit.html'
    model = Video
    fields = ['category', 'title', 'description', 'url', 'duration', 'created']
    success_url = reverse_lazy('admin2_videos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['categories'] = Category.objects.all()
        return context


class VideoDeleteView(generic.DeleteView):
    template_name = 'stream/video_delete.html'
    model = Video
    success_url = reverse_lazy('admin2_videos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
