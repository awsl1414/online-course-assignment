from io import BytesIO

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from crud import get_current_user
from utils import general_not_found, get_db, read_excel_to_dicts, insert_data_from_dicts


router_extension = APIRouter(tags=["扩展路由"])


@router_extension.post("/upload_file_by_excel/")
async def create_upload_file(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    file: UploadFile = File(...),
    model_name: str = None,
):
    from utils import model_mapping, base_mapping

    if model_name not in model_mapping:
        raise general_not_found()

    model_class = model_mapping[model_name]
    file_content = BytesIO(await file.read())
    data_list = read_excel_to_dicts(file_content, mapping=base_mapping[model_name])
    insert_data_from_dicts(db=db, model=model_class, data_list=data_list)
    return {"filename": file.filename}
