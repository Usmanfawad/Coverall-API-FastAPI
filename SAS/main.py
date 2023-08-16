from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from routers.api import router as router_api



###
# Main application file
###

def get_application() -> FastAPI:
    ''' Configure, start and return the application '''

    ## Start FastApi App
    application = FastAPI()

    ## Mapping api routes
    application.include_router(router_api, prefix="/api")

    ## Add exception handlers
    # application.add_exception_handler(HTTPException, http_error_handler)

    ## Allow cors
    application.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )

    ## Example of admin route
    # application.include_router(
    #     admin.router,
    #     prefix="/admin",
    #     tags=["admin"],
    #     dependencies=[Depends(get_token_header)],
    #     responses={418: {"description": "I'm a teapot"}},
    # )

    return application


app = get_application()