function loadPage() {
    let params = new URLSearchParams(document.location.search);
    let p = params.has('p') ? params.get('p') : ''
    let s = params.has('s') ? params.get('s') : ''
    if(!s)
        return
    $('#content').load(`/${p}/${s}.html`)
}

function sleep(s) {
    let ms = Number(s) * 1000
    return new Promise(resolve => setTimeout(resolve, ms))
}

function getCurrentTime() {
    let today = new Date()
    let time = today.getHours() + ":" + today.getMinutes()
    return time
}

function getCurrentDateTime() {
    let date = new Date();
    let datetime = date.toISOString().split('T')[0]
    datetime += ' ' + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds()
    return datetime
}