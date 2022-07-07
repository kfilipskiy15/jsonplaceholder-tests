from core.fixtures import *


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com/posts/",
    )


@fixture(scope="session", autouse=True)
def base_url(request):
    return request.config.getoption("--url")
