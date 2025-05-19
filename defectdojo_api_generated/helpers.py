from typing import TYPE_CHECKING, Any, Callable, Generator, Generic, TypeVar

from pydantic import BaseModel

if TYPE_CHECKING:
    from defectdojo_api_generated.api_client import ApiClient

T = TypeVar('T')
Z = TypeVar('Z')


class IteratorResult(BaseModel, Generic[T, Z]):
    result: T
    page: Z


def get_all_pages(
    api_client: 'ApiClient',
    api_list_method: Callable[..., T],
    *args: list[Any],
    **kwargs: dict[str, Any],
) -> Generator[T, None, None]:
    param_base = list(api_client.param_serialize('GET', '', auth_settings=['basicAuth', 'cookieAuth', 'tokenAuth']))

    page = api_list_method(*args, **kwargs)
    paginated_kls = page.__class__
    yield page

    while page.next:
        param_base[1] = page.next
        response = api_client.call_api(*param_base)
        page = paginated_kls.from_json(response.read())
        yield page
