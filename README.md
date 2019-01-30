Ported version of starlette to run on Python 3.5

# Install

python3 -m pip install git+https://github.com/em92/starlette

# Notes

Comparing to original starlette it doesn't give you:
1. 100% type annotated codebase
2. Zero hard dependencies.

Reasons of above is Python 3.5:
1. Till 3.5.4 exclusively does not have type annotation `typing.AsyncGenerator`. See commit `f691b60784abee7d4aa0fad3ef2da64783cb8c30`
2. `async_generator` package is required to port functions, that are used as async generators (yield inside async function is supported in 3.6+).
