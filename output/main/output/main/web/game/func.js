
async function start_game() {
    await eel.start()()
}

function openConsoleWindow() {
    window.open('/index.html?p=game&s=console', '訊息視窗', `width=300,height=500,top=0, left=${screen.width}`)
}

$.fn.appendVal = function (newPart) {
    return this.each(function(){ $(this).val( $(this).val() + newPart); })
};
$.fn.scrollBottom = function() {
    return $(this).scrollTop($(this)[0].scrollHeight)
};
function refreshConsole() {
    $("#textarea").val( $("#textarea").val()).scrollBottom()
}

eel.expose(consoleLog)
function consoleLog(message) {
    let datetime = getCurrentDateTime()
    message = `[ ${datetime} ] ` + message
    message += '\n'
    $('#textarea').appendVal(message)
    refreshConsole()
}
