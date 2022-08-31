async function addTask(time, type) {
    console.log(time)
    let res = await eel.taskadd(time, type)()
    res = JSON.parse(res)
    let code = res.code
    let msg = res.msg
    alert(msg)
    if(code) {
        location.reload()
    }
}

async function selectTask(id) {
    let res = await eel.taskselect(id)()
    res = JSON.parse(res)

    let code = res.code
    let msg = res.msg
	let task = res.task[0]

    let time = task[1]
    let type = task[2]

    $('#time').val(time)
    $('#type').val(type)
}

async function selectTasks(currentPage=1) {
    let res = await eel.taskselectall()()
    res = JSON.parse(res)
    console.log(res)
    let code = res.code
    let msg = res.msg
    let tasks = res.tasks
    let pageSize = 10
    renderPage(tasks, pageSize, currentPage)
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
        let time = user[1]
        let type = getTypeName(user[2])



        let template = `
                <tr role="row" class="odd">
            <td class="sorting_1">${time}</td>
            <td>${type}</td>
            <td>
            <div class="form-button-action">
            <button onclick="location.href='?p=task&s=task&mode=edit&id=${id}'" type="button" data-toggle="tooltip" title="" class="btn btn-link btn-primary btn-lg" data-original-title="Edit Task">
            <i class="fa fa-edit"></i>
            </button>
            <button onclick="deleteTask('${id}')" type="button" data-toggle="tooltip" title="" class="btn btn-link btn-danger" data-original-title="Remove">
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

async function editTask(id, time, type) {
    let res = await eel.taskedit(id, time, type)()
    res = JSON.parse(res)
    let code = res.code
    let msg = res.msg
    alert(msg)
    if(code) {
        history.go(-1)
    }
}


async function deleteTask(id) {
    let flag = confirm('您確定要刪除這項任務？');
    if (flag) {
        let res = await eel.taskdelete(id)()
        res = JSON.parse(res)
        let code = res.code
        let msg = res.msg
        alert(msg)
        if (code) {
            location.reload()
        }
    }
}


function getTypeName(type) {
    if (type == 'shutdown') {
            type = '關機'
    }
    return type
}