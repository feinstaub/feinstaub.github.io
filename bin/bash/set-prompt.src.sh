#
# references
#    exit code prompt: http://stackoverflow.com/questions/16715103/bash-prompt-with-last-exit-code
#    good bash structure: https://github.com/demure/dotfiles
#

# see http://stackoverflow.com/questions/4774054/reliable-way-for-a-bash-script-to-get-the-full-path-to-itself
# SCRIPTPATH=$( cd $(dirname $0) ; pwd -P ) # only works for non-sourced scripts
#http://unix.stackexchange.com/questions/4650/determining-path-to-sourced-shell-script
# !!!
SCRIPTPATH=$( cd $(dirname $_) ; pwd -P )
# echo "SCRIPTPATH.............. $SCRIPTPATH"

# KF5 check
function __is_kf5_env_set {
    # set local colors Variables
    source $SCRIPTPATH/colors-set-local.src.sh

    if [[ -z "$KF5" ]]; then # -z : value not set
        local subdir=~/dev/kf5
        if [ "${PWD##$subdir}" != "$PWD" ]; then # http://unix.stackexchange.com/questions/6435/how-to-check-if-pwd-is-a-subdirectory-of-a-given-path
            # reminds me when I am in the kf5 dev dir and the env is not properly set up
            echo -e "[${RED}NOT_kf5${RESETCOLOR}]"
        else
            # show nothing
            echo -e ""
        fi
    else
        echo -e "[${WHITEBOLD}KF5 set${RESETCOLOR}]"
    fi
}

# DEVUSR check (for kde4)
function __is_devusr_env_set {
    # set local colors Variables
    source $SCRIPTPATH/colors-set-local.src.sh

    if [[ -z "$DEVUSR" ]]; then # -z : value not set
        test # do nothing
    else
        echo -e "[${WHITEBOLD}DEVUSR=$DEVUSR${RESETCOLOR}]"
    fi
}

# python virutalenv check
function __is_pyvenv_set {
        source $SCRIPTPATH/colors-set-local.src.sh

    if [[ -n "$VIRTUAL_ENV" ]]; then # -n : value set
        echo -e "[${WHITEBOLD}$VIRTUAL_ENV${RESETCOLOR}]"
    else
        echo -e ""
    fi
}

# unset colors Variables
# source ~/system_suse/colors-unset.bash # will prevent colors from work

# orig:
# export PS1='\[$(ppwd)\]\u@\h:\w> '

# NEW:
export PROMPT_COMMAND=__prompt_command  # Func to gen PS1 after CMDs

#export PROMPT_COMMAND=__aaa

# function __aaa() {
#     echo "c"
#     __git_ps1 "a" "b"
#     echo "d"
# }

#
# see http://serverfault.com/questions/69312/automatically-change-the-gnome-terminal-title-for-the-window
# see http://wiki.ubuntuusers.de/Bash/Prompt
# see http://stackoverflow.com/questions/16715103/bash-prompt-with-last-exit-code
# see https://github.com/demure/dotfiles
#
function __prompt_command() {
    local EXIT="$?" # This needs to be first

    source $SCRIPTPATH/colors-set-local.src.sh

    if [ $EXIT != 0 ]; then
        # echo "Exit code meanings: see http://tldp.org/LDP/abs/html/exitcodes.html"
        EXITPART="${RED}$EXIT]${RESETCOLOR}$MYPS1" # Add red if exit code non 0
    else
        EXITPART="${GREEN}$EXIT]${RESETCOLOR}$MYPS1"
    fi

    # git PS1 prompt prepare
    source $SCRIPTPATH/git-prompt.src.sh # from https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh

    local GIT_PS1_SHOWDIRTYSTATE=1 # needs source ~/bash/git-prompt.src.sh # from https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
    local GIT_PS1_SHOWCOLORHINTS=1 # and are available only when using __git_ps1 for PROMPT_COMMAND or precmd

    # MYPS1='\[$(ppwd)\]'${WHITE}'\u'${RESETCOLOR}'@'${WHITE}'\h'${RESETCOLOR}'$(__is_kf5_env_set):\w$(__git_ps1 " (%s)")> '
    # MYPS1="$(__git_ps1 ${CYAN}[${RESETCOLOR}%s${CYAN}]${RESETCOLOR})"

    local USERHOSTPART=${WHITE}'\u'${RESETCOLOR}${WHITE}'@'${RESETCOLOR}${WHITE}'\h'${RESETCOLOR}
    local PREGIT='\[$(ppwd)\]'${EXITPART}${USERHOSTPART}$(__is_kf5_env_set)$(__is_devusr_env_set)$(__is_pyvenv_set)':'${YELLOW}'\w'${RESETCOLOR}
    local POSTGIT=$YELLOWBOLD'> '$RESETCOLOR

    __git_ps1 "$PREGIT" "$POSTGIT" "${WHITE}[${RESETCOLOR}%s${WHITE}]${RESETCOLOR}"

    # PS1=""
    # PS1+="${RCol}@${BBlu}\h ${Pur}\W${BYel}$ ${RCol}"
}
