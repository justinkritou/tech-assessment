FROM jupyter/datascience-notebook

MAINTAINER justinkritou@gmail.com

WORKDIR /home/jovyan/work

ADD . /home/jovyan/work
