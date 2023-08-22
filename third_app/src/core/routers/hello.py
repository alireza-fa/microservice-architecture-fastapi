from fastapi import APIRouter


router = APIRouter(prefix='/api/third')


@router.get('/hello/')
def say_hello():
    return 'Hello From Third app'
