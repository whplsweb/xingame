// 檢查授權

verify()

// 時間間隔為10分鐘
let time_interval = 1000 * 60 * 60 * 10
let verify_clock = setInterval(verify , time_interval);

// 載入側邊欄
$(document).ready(function() {
      $('#sidebar').load("/templates/sidebar.html")

      // 載入子頁面
      loadPage()
});

// 切換紅色主題
$('#buttonRed').click()
// 隱藏按鈕
$('.custom-toggle').hide()

async function verify() {
      let token = $.cookie('token')
      let res = await eel.verifyToken(token)()

      res = JSON.parse(res)
      console.log(res)

      let code = Number(res.code)
      let msg = res.msg

      if (!code) {
            alert(msg)
            location.href = '/login/login.html'
      }
}