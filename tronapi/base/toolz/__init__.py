try:
    from cytoolz import (
        assoc,
        complement,
        compose,
        concat,
        cons,
        curry,
        dicttoolz,
        dissoc,
        excepts,
        functoolz,
        groupby,
        identity,
        itertoolz,
        merge,
        partial,
        pipe,
        sliding_window,
        valfilter,
        valmap,
    )
except ImportError:
    from toolz import (  # noqa: F401
        assoc,
        complement,
        compose,
        concat,
        cons,
        curry,
        dicttoolz,
        dissoc,
        excepts,
        functoolz,
        groupby,
        identity,
        itertoolz,
        merge,
        partial,
        pipe,
        sliding_window,
        valfilter,
        valmap,
    )