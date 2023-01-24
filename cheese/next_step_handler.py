from pyflink.common import Time
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment, MapFunction, RuntimeContext, TimeWindow, KeyedProcessFunction
from pyflink.datastream.state import ValueStateDescriptor, StateTtlConfig


class NextStepHandler(KeyedProcessFunction):
    def __init__(self):
        self.state = None
        self.user_id = "ss01"
        self.step = [
            "odd", "even",
            "odd", "even",
            "odd", "even",
            "odd", "even",
            "odd", "even",
            "odd", "even",
            "odd", "even",
            "odd"
        ]
        self.MIN_AMOUNT = 100
        self.MAX_AMOUNT = 5_000_000
        self.RATIO = 2.2

    def open(self, runtime_context: RuntimeContext):
        state_descriptor = ValueStateDescriptor("state", Types.PICKLED_BYTE_ARRAY())
        # time to live
        state_ttl_config = StateTtlConfig.new_builder(Time.hours(24)).set_update_type(
            StateTtlConfig.UpdateType.OnReadAndWrite) \
            .disable_cleanup_in_background()

        state_descriptor.enable_time_to_live(state_ttl_config)
        self.state = runtime_context.get_state(state_descriptor=state_descriptor)

    def process_element(self, value, ctx: 'KeyedProcessFunction.Context'):
        # 0. user
        # 1. 알고리즘
        # 2. 배팅한 스텝
        # 3. 배팅한 금액

        current = self.state.value()

        if current is None:
            current = self.user_id, value[1], 0, self.MIN_AMOUNT

        self.state.update(current)










    def next_amount(self, current_amount):
        return int(current_amount * self.RATIO // 10 * 10)


