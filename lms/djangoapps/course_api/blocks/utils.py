from openedx.core.djangoapps.discussions.models import (
    DiscussionsConfiguration,
    Provider,
)


def filter_discussion_xblocks_from_response(response, course_key, request_from_mobile=False):
    """
    Removes discussion xblocks if request is from mobile and provider is openedx
    """
    configuration = DiscussionsConfiguration.get(context_key=course_key)
    provider = configuration.provider_type
    if provider == Provider.OPEN_EDX and request_from_mobile:
        blocks = response.data
        filtered_blocks = {}
        for key, value in blocks.get('blocks', {}).items():
            if value.get('type') != 'discussion':
                filtered_blocks[key] = value
        response.data['blocks'] = filtered_blocks
    return response
