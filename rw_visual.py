#!/bin/sh/python

# -*- conding: utf-8 -*-

# author xuyan
# 2018/05/17

import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show