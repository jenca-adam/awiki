def notraised(fun,error=Exception):
    try:
        fun()
        return True
    except error:
        return False
    except Exception:
        return True

