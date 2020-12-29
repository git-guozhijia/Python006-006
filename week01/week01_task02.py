import week01.logging_t,time,os
from pathlib import Path

CurrentTime = time.strftime("%Y-%m-%d", time.localtime())
PATH = f'./var/log/python-{CurrentTime}/log.log'

def task():
    path_t = '.'
    for i in os.path.dirname(PATH).split('/')[1:]:
        path_t = path_t + f'/{i}'
        if not os.path.exists(path_t):
            try:
                os.makedirs(path_t)
            except OSError as err:
                print(err)
    logger = week01.logging_t.log(PATH)
    logger.info(CurrentTime)

def task01():
    path_t = ''
    p = Path.joinpath(Path.cwd(), Path(PATH))
    for i in str(p.parent).split('/')[1:]:
        path_t = path_t + f'/{i}'
        if not Path(path_t).is_dir():
            Path(path_t).mkdir()
        elif not p.is_file():
            p.touch()
    logger = week01.logging_t.log(str(p))
    logger.info(CurrentTime)


if __name__ == "__main__":
    # task()
    task01()