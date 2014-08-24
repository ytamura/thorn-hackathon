#thorn hackathon

heroku/python/django/opencv to host face detection API

need to use custom buildpack for opencv to work:

```
heroku config:set BUILDPACK_URL=git://github.com/ytamura/heroku-buildpack-python-opencv-scipy.git
```