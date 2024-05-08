# mdyttt

mdyttt or markdown youtube tooltip is a script that inserts youtube statistics as a Material for Mkdocs tooltip


Add 'content.tooltips' to features in your mkdocs.yml like so
```
theme:
  name: material
  logo:  assets/logo.png
  features:
    - content.tooltips
```
You also need to setup the Google API
https://developers.google.com/youtube/v3/quickstart/python

Usage:
youtube.py -f markdown.md
