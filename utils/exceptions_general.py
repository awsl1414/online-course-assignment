from fastapi import HTTPException, status


# 定义异常信息
EXCEPTION_DETAILS = {
    "NotFound": "记录未找到",
    "Found": "记录已存在",
}


# 工厂函数创建异常
def create_http_exception(
    exception_name: str, status_code: int, exception_info: dict, headers=None, **kwargs
):
    detail = exception_info[exception_name]
    if callable(detail):
        detail = detail(**kwargs)
    return HTTPException(status_code=status_code, detail=detail, headers=headers)


def general_not_found():
    return create_http_exception(
        exception_name="NotFound",
        status_code=status.HTTP_404_NOT_FOUND,
        exception_info=EXCEPTION_DETAILS,
    )


def general_found():
    return create_http_exception(
        exception_name="Found",
        status_code=status.HTTP_409_CONFLICT,
        exception_info=EXCEPTION_DETAILS,
    )
