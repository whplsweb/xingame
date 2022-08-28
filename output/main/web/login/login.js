$('#key').val('S5UCy9ND')

init_login()

function init_login() {
    let content = {}
    content.title = '提示'
    content.message = '請於10分鐘內完成授權 否則程式將會自動關閉'
    // 授權成功
    content.icon = 'fas fa-info-circle';
    $.notify(content,{
        type: 'info',
        placement: {
            from: 'top',
            align: 'center'
        },
        time: 1000,
        delay: 0,
        hideTime: 100
    });
    let time_interval = 600000
    setTimeout(forceQuit,time_interval);
}

async function login() {
    let key = $('#key').val()
    let res = await eel.login(key)()
    res = JSON.parse(res)
    let code = res.code
    let msg = res.msg

    let content = {}
    content.title = '授權狀態'
    content.message = msg
    // 授權成功
    if (code) {
        content.icon = 'fas fa-check';
        $.notify(content,{
            type: 'success',
            placement: {
                from: 'top',
                align: 'center'
            },
            time: 1000,
            delay: 0,
            hideTime: 100
        });

        let token = res.token
        $.cookie('token', token, { path: '/' })

        setTimeout(function () {
            location.href = '/index.html'
        }, 3000)
    }
    // 授權失敗
    else {
        content.icon = 'fas fa-times';
        $.notify(content,{
            type: 'danger',
            placement: {
                from: 'top',
                align: 'center'
            },
            time: 1000,
        });
    }
}

async function forceQuit() {
    let content = {}
    content.title = '提示'
    content.message = '未於指定時間內完成授權 自動結束程式'
    // 授權成功
    content.icon = 'fas fa-times'
    $.notify(content,{
        type: 'danger',
        placement: {
            from: 'top',
            align: 'center'
        },
        time: 1000,
        delay: 0,
        hideTime: 100
    })
    setTimeout(Q, 5000)
}

async function Q() {
    window.open("about:blank","_self").close()
    await eel.quit()()
}