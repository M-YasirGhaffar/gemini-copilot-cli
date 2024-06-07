PROMPT_COMMAND='history -a; history -c; history -r'
exec > >(tee -ai $HOME/command_log.txt)
exec 2> >(tee -ai $HOME/command_log_err.txt >&2)
