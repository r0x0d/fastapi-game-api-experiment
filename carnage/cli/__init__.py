# https://github.com/python/typeshed/issues/7539#issuecomment-1076581049
import argparse
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    SubparserType = argparse._SubParsersAction[argparse.ArgumentParser]
else:
    SubparserType = Any
