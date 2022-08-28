// 自動點擊特效
let p = params.has('p') ? params.get('p') : ''
let c = $(`a[href="#${p}"]`).click()