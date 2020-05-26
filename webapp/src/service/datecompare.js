function compare(a, b) {
    a = a['date']
    b = b['date']
    let b_date = b.split("-")
    let a_date = a.split("-")
    let a_month = parseInt(a_date[0])
    let a_day = parseInt(a_date[1])
    let b_month = parseInt(b_date[0])
    let b_day = parseInt(b_date[1])
    if (a_month > b_month) {
        return 1
    } else if (a_month === b_month) {
        if (a_day > b_day) {
            return 1
        } else {
            return -1
        }
    } else {
        return -1
    }
}

export {
    compare
}