from typing import List
from app import schemas
import pytest

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    #posts = schemas.PostOut(res.json())
    def validate(post):
        return schemas.PostOut(**post)
    posts_map = map(validate, res.json())
    
    assert res.status_code == 200
    assert len(res.json()) == len(test_posts)

def test_unauthorized_user_get_all_posts(client, test_posts):
    res  = client.get("/posts/")
    assert res.status_code == 401

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content

@pytest.mark.parametrize("title, content, published", [
    ("aswesome new title", "awesome new content", True),
    ("Favorite pizza", "I love chicken", False)
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post("/posts", json={"title": title, "content": content, "published":published})
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post("/posts", json={"title": "some title", "content": "some content"})
    created_post = schemas.Post(**res.json())
    assert created_post.published == True

def test_delete_post_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 201

def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[0].id
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data['title']

