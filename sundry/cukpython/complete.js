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

    if (!actualTime) {
        console.log("공부한 시간을 입력해주세요.");
        return;
    }

    if (!attempts || attempts < 1) {
        console.log("강의 시청은 한 번 하신 걸로 설정합니다.", attempts);
    }

    function colonTimeToSeconds(colonTime) {
        console.log(colonTime);
        let times = colonTime.split(":");
        console.log(times);
        if (times.length > 3) {
            console.log("시간:분:초 단위로 입력해주세요.\nex) 1:02:31");
        }

        let result = 0;
        let length = times.length;
        for (let i = 0; i < length; i++) {
            result += addTimes(times.pop(), i);
        }
        console.log(result);
        return result + Math.round((Math.random() + Number.EPSILON) * 1000000) / 1000000;
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
