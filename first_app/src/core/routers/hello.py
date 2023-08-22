from fastapi import APIRouter


router = APIRouter(prefix='/api/first')


@router.get('/hello/')
def say_hello():
    return 'Hello From First App'
