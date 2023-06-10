# Save the last command.
CHEERUP_LAST_COMMAND=""

preexec() {
    CHEERUP_LAST_COMMAND=$1
}

precmd() {
    # Prevent cheerup command from running on itself.
    if [[ "$CHEERUP_LAST_COMMAND" != "cheerup -c"* ]]; then
        cheerup -c "$CHEERUP_LAST_COMMAND"
    fi
}
