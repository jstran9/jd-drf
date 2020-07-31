from rest_framework import serializers

from .models import Post

from django import forms


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description', 'owner'
        )

# to create a form.. (below)
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = (
#             'title', 'description'
#         )

