async function addUser(username, password, direct, molo) {
    let res = await eel.useradd(username, password, direct, molo)()
    res = JSON.parse(res)
    let code = res.code
    let msg = res.msg
    alert(msg)
    if(code) {
        location.reload()
    }
}

async function selectUser(id) {
    let res = await eel.userselect(id)()
    res = JSON.parse(res)
    let code = res.code
    let msg = res.msg
	let user = res.user[0]

    let username = user[1]
    let password = user[2]
    let direct = user[3]
    let molo = user[4]
    if (direct)
        $('#direct').prop('checked', true)
    if (molo)
        $('#molo').prop('checked', true)
    $('#username').val(username)
    $('#password').val(password)
}

async function selectUsers(currentPage=1) {
    let res = await eel.userselectall()()
    res = JSON.parse(res)
    let code = res.code
    let msg = res.msg
    let users = res.users
    let pageSize = 10
    renderPage(users, pageSize, currentPage)
}

function getURLWithout(p) {
    let url = window.location.href.split('?')[0] + '?'
    const urlSearchParams = new URLSearchParams(window.location.search);
    const params = Object.fromEntries(urlSearchParams.entries());
    Object.keys(params).forEach(function(key) {
        if (key!=p) {
            let value = params[key]
            url += `${key}=${value}&`
        }
    });
    return url
}

function renderPage(data, pageSize, currentPage=1) {
    $('#tbody').empty()
    $('.pagination').empty()
    let pagination_res = pagination(data, pageSize, currentPage)
    let data_size = pagination_res.data.length-1
    let pagination_users = data_size ? pagination_res.data : 0
    let pagination_fist_data = data_size ? pagination_res.firstData : 0
    let pagination_last_data = data_size ? pagination_res.lastData : 0
    let pagination_total_pages = data_size ? pagination_res.totalPages : 0
    let pagination_total_data_current = data_size ? pagination_res.dataCurrent : 0
    if(data_size){

    for (let i = 1; i <= pagination_total_data_current; i++) {
        let user = pagination_users[i]
        let id = user[0]
        let username = user[1]
        let password = user[2]
        let template = `
                <tr role="row" class="odd">
            <td class="sorting_1">${username}</td>
            <td>${password}</td>
            <td>
            <div class="form-button-action">
            <button onclick="location.href='?p=account&s=user&mode=edit&id=${id}'" type="button" data-toggle="tooltip" title="" class="btn btn-link btn-primary btn-lg" data-original-title="Edit Task">
            <i class="fa fa-edit"></i>
            </button>
            <button onclick="deleteUser('${id}')" type="button" data-toggle="tooltip" title="" class="btn btn-link btn-danger" data-original-title="Remove">
            <i class="fa fa-times"></i>
            </button>
            </div>
            </td>
            </tr>`
        $('#tbody').append(template)
    }
    }


    // 渲染 Page
    $('#show_first_last_data_text').text(`展示 ${pagination_fist_data} 至 ${pagination_last_data} 筆數據`)

    // 取得所有參數 除了"page以外"的參數 的URL
    let url = getURLWithout('page')

    // 前一頁
    let previous_page = Number(currentPage)-1
    if (previous_page >= 1)
    {
        $('.pagination').append(`<li class="paginate_button page-item previous" id="add-row_previous"><a href="${url}page=${previous_page}" aria-controls="add-row" data-dt-idx="0" tabindex="0" class="page-link">上一頁</a></li>`)
    }
    for (let page = 1; page<=pagination_total_pages; page++) {
        // 內頁
        if (page == currentPage)
        {
            $('.pagination').append(`<li class="paginate_button page-item active"><a href="${url}page=${page}" aria-controls="add-row" data-dt-idx="1" tabindex="0" class="page-link">${page}</a></li>`)
        }
        else
        {
            $('.pagination').append(`<li class="paginate_button page-item"><a href="${url}page=${page}" aria-controls="add-row" data-dt-idx="1" tabindex="0" class="page-link">${page}</a></li>`)
        }
    }
    // 下一頁
    let next_page = Number(currentPage)+1
    if (next_page <= pagination_total_pages)
    {
        $('.pagination').append(`<li class="paginate_button page-item previous" id="add-row_previous"><a href="${url}page=${next_page}" aria-controls="add-row" data-dt-idx="0" tabindex="0" class="page-link">下一頁</a></li>`)
    }
}

async function editUser(id, username, password, direct, molo) {
    let res = await eel.useredit(id, username, password, direct, molo)()
    res = JSON.parse(res)
    let code = res.code
    let msg = res.msg
    alert(msg)
    if(code) {
        history.go(-1)
    }
}


async function deleteUser(id) {
    let flag = confirm('您確定要刪除這隻帳號？');
    if (flag) {
        let res = await eel.userdelete(id)()
        res = JSON.parse(res)
        let code = res.code
        let msg = res.msg
        alert(msg)
        if (code) {
            location.reload()
        }
    }
}

async function mimicSearch(username) {
    let res = await eel.mimicsearch(username)()
    res = JSON.parse(res)
    let code = res.code
    let msg = res.msg
    let users = res.users
    let pageSize = 10
    renderPage(users, pageSize)
}

