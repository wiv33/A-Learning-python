/**
 * 1. 전체 코드 개발자 도구에서 붙여 넣기.
 * 2. complete 함수 호출하기.
 * @param trackId
 * @param actualTime
 * @param attempts
 */
function complete(trackId, actualTime, attempts) {
    if (!trackId || trackId < 1) {
        console.log("track id는 필수입니다.");
        return;
    }

    if (!actualTime || actualTime.split(":").length > 3 || actualTime.split(":").length < 2) {
        console.log("공부한 시간을 시간:분:초 단위로 입력해주세요.\nex) 1:02:31");
        return;
    }

    if (!attempts || attempts < 1) {
        console.log("강의 시청은 한 번 하신 걸로 설정합니다.", attempts);
    }

    function colonTimeToSeconds(colonTime) {
        console.log("공부한 시간 # ", colonTime);
        let times = colonTime.split(":");
        let totalSeconds = 0;
        let length = times.length;
        for (let i = 0; i < length; i++) {
            totalSeconds += addTimes(times.pop(), i);
        }
        let result = totalSeconds + Math.round((Math.random() + Number.EPSILON) * 1000000) / 1000000;
        console.log("최종 공부한 초: ", result);
        return result;
    }

    function addTimes(times, count) {
        let result = 1;
        for (let i = 0; i < count; i++) {
            result *= 60;
        }
        return times * result
    }

    $('head').append('<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">');
    let obj = {
        "type": "vod_track_for_onwindow",
        "track": trackId,
        "state": 99,
        "position": colonTimeToSeconds(actualTime),
        "attempts": attempts ? attempts : 1,
        "interval": 60000
    };
    let res = []
    for (let key in obj) {
        res.push(key + '=' + obj[key]);
    }
    $.ajax({
        url: '/mod/vod/action.php',
        type: 'POST',
        data: res.join("&"),
        dataType: 'json'
    }).done(data => {
        console.log(data);
    })
}
