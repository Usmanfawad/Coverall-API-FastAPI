from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from SAS.db.session import engine
from SAS.db.base import Base

from SAS.routers.api import router as router_api
from SAS.routes import router as main_route

###
# Main application file
###

def create_tables():
	Base.metadata.create_all(bind=engine)

def get_application() -> FastAPI:
    ''' Configure, start and return the application '''

    ## Start FastApi App
    application = FastAPI()

    # Creating all database tables
    create_tables()


    ## Mapping api routes
    application.include_router(main_route)
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