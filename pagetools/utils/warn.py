import warnings
import inspect
import colorama
def warn(msg):
    f=inspect.currentframe().f_back.f_code
    prefix=colorama.Fore.MAGENTA+f.co_filename+colorama.Fore.RESET+' : '+colorama.Fore.CYAN+co_name+colorama.Fore.RED
    warnings.warn(
            prefix+msg+colorama.Fore.RESET
            )
