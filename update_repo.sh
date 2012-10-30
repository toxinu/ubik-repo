#!/bin/bash

ubik-repo generate
git add . && git commit -am "Update repo" && git push heroku master
