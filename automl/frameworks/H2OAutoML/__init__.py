from automl.utils import call_script_in_same_dir, dir_of


def setup(*args):
    call_script_in_same_dir(__file__, "setup.sh", *args)


def run(*args, **kwargs):
    from .exec import run
    run(*args, **kwargs)


def docker_commands():
    return """
RUN {here}/setup.sh
EXPOSE 54321
EXPOSE 54322
""".format(here=dir_of(__file__, True))


__all__ = (setup, run, docker_commands)
