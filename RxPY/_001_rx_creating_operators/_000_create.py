from rx import create

"""observable 순서 확인
Java의 publisher / subscriber
required: onNext
optional: [on_complete | on_error]
"""


def create_one_next_observable(observer, scheduler):
    observer.on_next("hello")


def create_complete_observable(observer, scheduler):
    observer.on_next("hello")
    observer.on_completed()
    observer.on_error("Error occurred")


def create_error_observable(observer, scheduler):
    observer.on_next("hello")
    observer.on_error("Error occurred")
    observer.on_completed()


one_next = create(create_one_next_observable)
complete = create(create_complete_observable)
error = create(create_error_observable)

complete.subscribe(
    on_next=lambda i: print("Got - {0}".format(i)),
    on_completed=lambda: print("on Complete"),
    on_error=lambda e: print("Error: {}".format(e)),
)

error.subscribe(
    on_next=lambda i: print("Got - {0}".format(i)),
    on_completed=lambda: print("on Complete"),
    on_error=lambda e: print("Error: {}".format(e)),
)

one_next.subscribe(
    on_next=lambda i: print("Got - {0}".format(i)),
    on_completed=lambda: print("on Complete"),
    on_error=lambda e: print("Error: {}".format(e)),
)
