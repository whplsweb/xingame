function pagination(data, pageSize, currentPage=1) {
  currentPage = (currentPage == '') ? 1 : currentPage
  let dataTotal = data.length
  // 總資料數 換㔯 頁數 公式
  let pageTotal = Math.ceil(dataTotal / pageSize)

  // 若 當前頁數 = 最大頁數 則 最大頁數
  if (currentPage > pageTotal) {
    currentPage = pageTotal;
  }

  // 第 i 筆  ~ 第 i + currentPage 筆

  // i
  let firstData = (currentPage * pageSize) - pageSize + 1
  // i + currentPage
  let lastData = (currentPage * pageSize)

  if (lastData > dataTotal) {
      lastData = dataTotal
  }

  let res = {
    'data': [{}],
    'firstData': firstData,
    'lastData': lastData,
    'totalPages': pageTotal,
    'dataCurrent': lastData-firstData+1
  }


  if(data){
    data.forEach((item, index) => {
      // 獲取陣列索引，但因為索引是從 0 開始所以要 +1。
      const num = index + 1;

      // 這邊判斷式會稍微複雜一點
      // 當 num 比 minData 大且又小於 maxData 就push進去新陣列。
      if ( num >= firstData && num <= lastData) {
        res.data.push(item)
      }
    })
  }
  return res
}
