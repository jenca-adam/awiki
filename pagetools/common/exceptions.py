class AwikiError(Exception):pass
class EmptyBIBError(AwikiError):pass
class LoadingError(AwikiError):pass
class PageExistsError(LoadingError,FileExistsError):pass
