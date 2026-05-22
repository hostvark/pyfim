from invoke import task


@task
def find_cache(c):
    command = (
        r'''find . -name ".venv" -prune -o \( -type d '''
        r'''-name "__pycache__" -o -type d '''
        r'''-name ".pytest_cache" \)'''
    )
    c.run(command)


@task
def clear_cache(c):
    command = (
        r'''find . -name ".venv" -prune -o \( -type d '''
        r'''-name "__pycache__" -o -type d '''
        r'''-name ".pytest_cache" \) '''
        r'''-exec rm -rf {} +'''
    )
    c.run(command)
