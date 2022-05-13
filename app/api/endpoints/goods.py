from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db_setup import Session, get_db
from app.models.good import Good
from app.crud import crud_goods
from app.schemas import goods_schema

router = APIRouter()

@router.get('/')
def get_goods():
    pass

@router.get('/{id}')
def get_goods_by_id(id=id):
    return id

@router.post('/', response_model=goods_schema.GoodsBase)
def add_goods(*,
              db:Session =  Depends(get_db),
              goods: goods_schema.GoodsBase):
    goods = crud_goods.goods.create(db=db,obj_in=goods)
    return goods
    
    
@router.put('/{id}')
def update_goods(id=id):
    pass

@router.delete('/{id}')
def delete_goods(id=id):
    pass