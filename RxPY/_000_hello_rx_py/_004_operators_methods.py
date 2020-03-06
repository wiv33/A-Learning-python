import rx
from rx import operators as op

"""Creating"""
rx.create()
rx.empty()
rx.never()
rx.throw()
rx.interval()
rx.from_()
rx.interval()
rx.just()
rx.range()
rx.repeat_value()
rx.start()
rx.timer()

"""Mathematical"""
op.average()
op.concat()
op.count()
op.max()
op.min()
op.reduce()
op.sum()

"""Transformation"""
op.buffer()
op.group_by()
op.map()
op.scan()
# ...

"""Filtering"""
op.debounce()
op.distinct()
op.filter()
op.element_at()
op.first()
op.ignore_elements()
op.last()
op.skip()
op.skip_last()
op.take()
op.take_last()
# ...

"""Error Handling"""
op.catch()
op.retry()

"""Utility"""
op.delay()
op.materialize()
op.time_interval()
op.timeout()
op.timestamp()

"""Conditional and Boolean"""
op.all()
op.contains()
op.default_if_empty()
op.sequence_equal()
op.skip_until()
op.skip_while()
op.take_until()
op.take_while()

"""Connectable"""
op.publish()
op.ref_count()
op.replay()

"""Combining"""
op.combine_latest()
op.merge()
op.start_with()
op.zip()
