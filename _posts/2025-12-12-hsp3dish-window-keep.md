---
layout: post
title: HSP3Dishで画面外にウィンドウを映すと白くなる問題の回避方法
date: 2025-12-12 19:12:47 +09:00
author: ABATBeliever
tags: [HSP3, Tips, 入門, hsp3dish]
summary: oncmdを使うことで、hsp3dishでウィンドウを画面外に持って行った時に白くなるのを阻止します。
---

## はじめに

oncmdを使うことで、hsp3dishでウィンドウを画面外に持って行った時にウィンドウが白くなるのを阻止します。

```
#include "hsp3dish.as"

#const WM_MOVE 0x0003
oncmd gosub *cmd, WM_MOVE

*main
    redraw 0
    color 255,0,0: boxf
    redraw 1
    await 1000/30
goto *main

*cmd
    redraw 0
    color 0,0,255: boxf
    redraw 1
return
```
