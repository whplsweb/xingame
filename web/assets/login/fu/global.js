
$(document).ready(function () {
    if (!ReadCookie('cookie_policy_accepted')) {
        if ($('#cookie-allowance').length != 0) {
            $('#cookie-allowance').css('display', 'block');
        }
        if ($('#header-group-cookie').length != 0) {
            $('#header-group-cookie').css('display', 'block');
        }
    }

    if (!ReadCookie('FujitsuWebsite_common_01'))
        SetJPcookie();
});

function SetCookie(cookie_name, cookie_value, cookie_days_alive) {
    var exdate = new Date();
    
    var hostname = location.hostname;
    hostname = hostname.substr(hostname.indexOf(".fujitsu"));
    exdate.setDate(exdate.getDate() + cookie_days_alive);
    var pathname = window.location.pathname;
    var path = '/';
    pathname = pathname.split('/');
    if (pathname) {
        if (pathname.length >= 2) {
            path += pathname[1];
        }
    }
    var c_value = escape(cookie_value) + ((cookie_days_alive == null) ? "" : "; expires=" + exdate.toUTCString()) + "; path=" + path + "; domain=" + hostname.toString();
    document.cookie = cookie_name + "=" + c_value;

}

function ReadCookie(cookie_name) {
    var i, x, y, ARRcookies = document.cookie.split(";");
    for (i = 0; i < ARRcookies.length; i++) {
        x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
        y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
        x = x.replace(/^\s+|\s+$/g, "");
        if (x == cookie_name) {
            return unescape(y);
        }
    }
}

function SetCookieAllowance() {
    SetCookie('cookie_policy_accepted', 'true', 999);
    window.location.reload();
    if ($('#cookie-allowance').length != 0) {
        $('#cookie-allowance').css('display:none');
    }
    if ($('#header-group-cookie').length != 0) {
        $('#header-group-cookie').css('display:none');
    }
}

/*----------------Cookies start --------------*/
if (typeof String.prototype.startsWith != 'function') {
    String.prototype.startsWith = function (str) {
        return this.substring(0, str.length) === str;
    }
};
function SetJPcookie() {
    var hostname = location.hostname;
    hostname = hostname.substr(hostname.indexOf(".fujitsu"));
    var URL = window.location.pathname
    if (URL.startsWith("/jp/") && (!URL.startsWith("/jp/group/"))) {
        var d = new Date();
        var exdate = new Date();
        exdate.setDate(exdate.getDate() + 1825);

        var milisecvalue = (d.getTime() - d.getMilliseconds()) / 1000
        var remdomvalue = Math.floor(Math.random() * 999999999 + 100000000)
        var cookie_value = 'OIC' + milisecvalue + '.' + remdomvalue;
        var cookie_Name = "FujitsuWebsite_common_01"
        var c_value = cookie_value + "; expires=" + exdate.toUTCString() + "; path=/; domain=" + hostname.toString();
        document.cookie = cookie_Name + "=" + c_value;
    }
}
/*--------------------End Cookies ------------------*/
