#!/bin/bash

# see http://blog.bigdinosaur.org/easy-ps1-colors/

#Prompt and prompt colors
# 30m - Black
# 31m - Red
# 32m - Green
# 33m - Yellow
# 34m - Blue
# 35m - Purple
# 36m - Cyan
# 37m - White
# 0 - Normal
# 1 - Bold
#   BLACK="\[\033[0;30m\]"
#   BLACKBOLD="\[\033[1;30m\]"
#   RED="\[\033[0;31m\]"
#   REDBOLD="\[\033[1;31m\]"
#   GREEN="\[\033[0;32m\]"
#   GREENBOLD="\[\033[1;32m\]"
#   YELLOW="\[\033[0;33m\]"
#   YELLOWBOLD="\[\033[1;33m\]"
#   BLUE="\[\033[0;34m\]"
#   BLUEBOLD="\[\033[1;34m\]"
#   PURPLE="\[\033[0;35m\]"
#   PURPLEBOLD="\[\033[1;35m\]"
#   CYAN="\[\033[0;36m\]"
#   CYANBOLD="\[\033[1;36m\]"
#   WHITE="\[\033[0;37m\]"
#   WHITEBOLD="\[\033[1;37m\]"
## export PS1="\n$BLACKBOLD[\t]$GREENBOLD \u@\h\[\033[00m\]:$BLUEBOLD\w\[\033[00m\] \\$ "
## }
## prompt

# use within a function

# \e  ASCII escape Zeichen (033)
# \[    Beginn einer Sequenz von nicht-darstellbaren Zeichen

local BLACK='\[\e[0;30m\]'
local BLACKBOLD='\[\e[1;30m\]'
local RED='\[\e[0;31m\]'
local REDBOLD='\[\e[1;31m\]'
local GREEN='\[\e[0;32m\]'
local GREENBOLD='\[\e[1;32m\]'
local YELLOW='\[\e[0;33m\]'
local YELLOWBOLD='\[\e[1;33m\]'
local BLUE='\[\e[0;34m\]'
local BLUEBOLD='\[\e[1;34m\]'
local PURPLE='\[\e[0;35m\]'
local PURPLEBOLD='\[\e[1;35m\]'
local CYAN='\[\e[0;36m\]'
local CYANBOLD='\[\e[1;36m\]'
local WHITE='\[\e[0;37m\]'
local WHITEBOLD='\[\e[1;37m\]'

#local RESETCOLOR='\[\e[0;00m\]'
local RESETCOLOR='\[\e[0m\]'

# other def:
#     local RCol='\[\e[0m\]'
#
#     local Red='\[\e[0;31m\]'
#     local Gre='\[\e[0;32m\]'
#     local BYel='\[\e[1;33m\]'
#     local BBlu='\[\e[1;34m\]'
#     local Pur='\[\e[0;35m\]'
