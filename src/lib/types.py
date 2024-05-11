# external imports
from pydantic import BaseModel

# internal imports


# define the request body
class RequestBody(BaseModel):
    """Request body for the POST request.

    Args:
    ----
        content (str): The content of the request

    """

    content: str


# define the response body
class ResponseBody(BaseModel):
    """Response body for the POST request.

    Args:
    ----
        message (str): The message to return

    """

    message: str
