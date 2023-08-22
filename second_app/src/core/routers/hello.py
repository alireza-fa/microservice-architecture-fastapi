from fastapi import APIRouter


router = APIRouter(prefix='/api/second')


@router.get('/hello/')
def say_hello():
    return 'Hello From Second app'
