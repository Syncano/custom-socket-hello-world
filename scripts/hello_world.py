content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Hello world!</title>
    </head>

    <body>
        Hello World!
    </body>
</html>
"""

set_response(HttpResponse(status_code=200, content=content, content_type='text/html'))
